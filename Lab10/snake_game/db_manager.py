import psycopg2
from db_config import connect

class SnakeDbManager:
    def __init__(self):
        self.conn = connect()
        if self.conn is not None:
            self.cursor = self.conn.cursor()
            self.create_tables()
        else:
            print("Failed to connect to the database")
            exit(1)

    def create_tables(self):
        """Create the necessary tables if they don't exist"""
        create_users_table = '''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        '''

        create_scores_table = '''
        CREATE TABLE IF NOT EXISTS user_scores (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            score INTEGER NOT NULL,
            level INTEGER NOT NULL,
            game_state JSONB,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        '''

        try:
            self.cursor.execute(create_users_table)
            self.cursor.execute(create_scores_table)
            self.conn.commit()
            print("Database tables created successfully.")
        except (Exception, psycopg2.Error) as error:
            print(f"Error creating tables: {error}")
            self.conn.rollback()

    def user_exists(self, username):
        """Check if a user exists"""
        query = "SELECT id FROM users WHERE username = %s;"
        self.cursor.execute(query, (username,))
        return self.cursor.fetchone() is not None

    def get_user_id(self, username):
        """Get user ID by username"""
        query = "SELECT id FROM users WHERE username = %s;"
        self.cursor.execute(query, (username,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def create_user(self, username):
        """Create a new user"""
        try:
            query = "INSERT INTO users (username) VALUES (%s) RETURNING id;"
            self.cursor.execute(query, (username,))
            user_id = self.cursor.fetchone()[0]
            self.conn.commit()
            return user_id
        except (Exception, psycopg2.Error) as error:
            print(f"Error creating user: {error}")
            self.conn.rollback()
            return None

    def get_user_level(self, user_id):
        """Get the highest level achieved by a user"""
        query = '''
        SELECT MAX(level) FROM user_scores
        WHERE user_id = %s;
        '''
        try:
            self.cursor.execute(query, (user_id,))
            result = self.cursor.fetchone()
            # Return 1 if no level found (new user or no scores yet)
            return result[0] if result and result[0] is not None else 1
        except (Exception, psycopg2.Error) as error:
            print(f"Error getting user level: {error}")
            return 1

    def get_high_score(self, user_id, level=None):
        """Get the highest score achieved by a user, optionally filtered by level"""
        try:
            if level is not None:
                query = '''
                SELECT MAX(score) FROM user_scores
                WHERE user_id = %s AND level = %s;
                '''
                self.cursor.execute(query, (user_id, level))
            else:
                query = '''
                SELECT MAX(score) FROM user_scores
                WHERE user_id = %s;
                '''
                self.cursor.execute(query, (user_id,))
                
            result = self.cursor.fetchone()
            return result[0] if result and result[0] is not None else 0
        except (Exception, psycopg2.Error) as error:
            print(f"Error getting high score: {error}")
            return 0

    def save_score(self, user_id, score, level, game_state=None):
        """Save a user's score and game state"""
        try:
            if game_state:
                query = '''
                INSERT INTO user_scores (user_id, score, level, game_state)
                VALUES (%s, %s, %s, %s)
                RETURNING id;
                '''
                self.cursor.execute(query, (user_id, score, level, game_state))
            else:
                query = '''
                INSERT INTO user_scores (user_id, score, level)
                VALUES (%s, %s, %s)
                RETURNING id;
                '''
                self.cursor.execute(query, (user_id, score, level))
                
            score_id = self.cursor.fetchone()[0]
            self.conn.commit()
            return score_id
        except (Exception, psycopg2.Error) as error:
            print(f"Error saving score: {error}")
            self.conn.rollback()
            return None

    def get_latest_saved_game(self, user_id):
        """Get the latest saved game state for a user"""
        query = '''
        SELECT game_state, level, score FROM user_scores
        WHERE user_id = %s AND game_state IS NOT NULL
        ORDER BY created_at DESC
        LIMIT 1;
        '''
        try:
            self.cursor.execute(query, (user_id,))
            return self.cursor.fetchone()
        except (Exception, psycopg2.Error) as error:
            print(f"Error getting saved game: {error}")
            return None

    def close_connection(self):
        """Close the database connection"""
        if self.conn:
            if self.cursor:
                self.cursor.close()
            self.conn.close()
            print("PostgreSQL connection closed.") 
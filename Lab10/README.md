# Lab 10 - PostgreSQL with Python

This lab consists of two applications that use PostgreSQL databases:

1. PhoneBook - A console-based phone book application
2. Snake Game - A pygame-based game with user accounts and score tracking

## Requirements

- Python 3.8 or higher
- Docker and Docker Compose (for database setup)
- Required Python packages (see requirements.txt in each application directory)

## Database Setup with Docker

The project includes a Docker Compose configuration to easily set up PostgreSQL and Redis databases:

```bash
# Start the database containers
docker-compose up -d

# Check if containers are running
docker-compose ps
```

The PostgreSQL database will be available at:

- Host: localhost
- Port: 5432
- Database: postgresdb
- Username: username
- Password: password

### Testing Database Connection

After starting the Docker containers, you can test the database connection using the provided script:

```bash
python test_db_connection.py
```

This will verify that both applications can connect to the PostgreSQL database.

## Setup

1. Start the PostgreSQL database using Docker Compose as described above.
2. If needed, modify the `database.ini` file in each application directory to match your PostgreSQL credentials.
3. Install the required packages:

```bash
cd phonebook
pip install -r requirements.txt

cd ../snake_game
pip install -r requirements.txt
```

## PhoneBook Application

The PhoneBook application provides the following functionality:

1. Add a new contact
2. Upload contacts from a CSV file
3. Update contact information
4. Search contacts with different filters
5. View all contacts
6. Delete contacts by name or phone number

### Running the PhoneBook

```bash
cd phonebook
python phonebook.py
```

### CSV Format

To upload contacts from a CSV file, the file should have the following format:

```
first_name,last_name,phone
John,Doe,+7747474747
Jane,Smith,+7757575757
```

A sample CSV file (`sample_contacts.csv`) is provided for testing.

## Snake Game

The Snake Game features:

1. User accounts that track progress
2. Multiple levels with increasing difficulty
3. Pause and save functionality (press 'P')
4. High score tracking per user and level

### Running the Snake Game

```bash
cd snake_game
python snake_game.py
```

### Game Controls

- Arrow keys to move the snake
- Press 'P' to pause the game and save current state
- The user must enter their username before playing
- Level selection is based on user progress (new levels unlock as you advance)

## Database Tables

### PhoneBook Tables

- `phonebook` - Stores contact information

### Snake Game Tables

- `users` - Stores user account information
- `user_scores` - Stores scores, levels, and saved game states

## Shutting Down

To stop the database containers:

```bash
docker-compose down
```

To stop the containers and remove the volumes (will delete all data):

```bash
docker-compose down -v
```

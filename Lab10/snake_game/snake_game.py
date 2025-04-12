import pygame
import random
import json
import sys
from db_manager import SnakeDbManager

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Game speed by level
SPEEDS = {
    1: 10,   # Easy level
    2: 15,   # Medium level
    3: 20    # Hard level
}

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 20)
large_font = pygame.font.SysFont('Arial', 40)

class Snake:
    def __init__(self, level=1):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT
        self.next_direction = RIGHT
        self.score = 0
        self.level = level
        self.walls = self.create_walls()
        self.food = self.generate_food()
        self.paused = False
        self.game_over = False
        
    def create_walls(self):
        walls = []
        
        # Different wall patterns based on level
        if self.level == 1:
            # Level 1: No internal walls, just boundaries
            pass
        elif self.level == 2:
            # Level 2: Some obstacles in the middle
            for i in range(5):
                walls.append((GRID_WIDTH // 4, GRID_HEIGHT // 2 + i))
                walls.append((GRID_WIDTH // 4 * 3, GRID_HEIGHT // 2 - i))
        elif self.level == 3:
            # Level 3: More complex walls
            for i in range(8):
                walls.append((GRID_WIDTH // 4, GRID_HEIGHT // 3 + i))
                walls.append((GRID_WIDTH // 4 * 3, GRID_HEIGHT // 3 + i))
                if i < 5:
                    walls.append((GRID_WIDTH // 2 - i, GRID_HEIGHT // 2))
                    walls.append((GRID_WIDTH // 2 + i, GRID_HEIGHT // 2))
                
        return walls
    
    def get_head_position(self):
        return self.positions[0]
    
    def move(self):
        if not self.paused and not self.game_over:
            self.direction = self.next_direction
            head_x, head_y = self.get_head_position()
            dir_x, dir_y = self.direction
            new_head = ((head_x + dir_x) % GRID_WIDTH, (head_y + dir_y) % GRID_HEIGHT)
            
            # Game over if collision with self or wall
            if (new_head in self.positions[1:] or 
                new_head in self.walls or 
                new_head[0] < 0 or new_head[0] >= GRID_WIDTH or 
                new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
                self.game_over = True
                return
            
            self.positions.insert(0, new_head)
            
            # If food is eaten, new food appears
            if new_head == self.food:
                self.score += 10
                self.food = self.generate_food()
            else:
                self.positions.pop()
    
    def generate_food(self):
        food = None
        while food is None or food in self.positions or food in self.walls:
            food = (
                random.randint(0, GRID_WIDTH - 1),
                random.randint(0, GRID_HEIGHT - 1)
            )
        return food
    
    def draw(self, surface):
        # Draw walls
        for position in self.walls:
            rect = pygame.Rect(
                position[0] * GRID_SIZE, 
                position[1] * GRID_SIZE, 
                GRID_SIZE, GRID_SIZE
            )
            pygame.draw.rect(surface, GRAY, rect)
            
        # Draw food
        rect = pygame.Rect(
            self.food[0] * GRID_SIZE, 
            self.food[1] * GRID_SIZE, 
            GRID_SIZE, GRID_SIZE
        )
        pygame.draw.rect(surface, RED, rect)
        
        # Draw snake
        for i, position in enumerate(self.positions):
            color = GREEN if i == 0 else BLUE  # Head is GREEN, body is BLUE
            rect = pygame.Rect(
                position[0] * GRID_SIZE, 
                position[1] * GRID_SIZE, 
                GRID_SIZE, GRID_SIZE
            )
            pygame.draw.rect(surface, color, rect)
    
    def handle_keys(self, key):
        if key == pygame.K_UP and self.direction != DOWN:
            self.next_direction = UP
        elif key == pygame.K_DOWN and self.direction != UP:
            self.next_direction = DOWN
        elif key == pygame.K_LEFT and self.direction != RIGHT:
            self.next_direction = LEFT
        elif key == pygame.K_RIGHT and self.direction != LEFT:
            self.next_direction = RIGHT
        elif key == pygame.K_p:  # Pause game with 'p' key
            self.paused = not self.paused
            return True  # Signal that pause key was pressed
        return False
    
    def to_dict(self):
        """Convert the game state to a dictionary for saving"""
        return {
            'positions': self.positions,
            'direction': self.direction,
            'next_direction': self.next_direction,
            'score': self.score,
            'level': self.level,
            'food': self.food,
            'walls': self.walls
        }
    
    @classmethod
    def from_dict(cls, state_dict):
        """Create a snake instance from a saved state dictionary"""
        snake = cls(level=state_dict['level'])
        snake.positions = state_dict['positions']
        snake.direction = tuple(state_dict['direction'])
        snake.next_direction = tuple(state_dict['next_direction'])
        snake.score = state_dict['score']
        snake.food = tuple(state_dict['food'])
        snake.walls = [tuple(wall) for wall in state_dict['walls']]
        return snake

def get_username():
    """Get the username from the user"""
    input_box = pygame.Rect(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2, SCREEN_WIDTH // 2, 40)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
                
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if text:  # Only accept if text is not empty
                            done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                        
        screen.fill(BLACK)
        
        # Render the prompt text
        prompt_surface = large_font.render('Enter your username:', True, WHITE)
        prompt_rect = prompt_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
        screen.blit(prompt_surface, prompt_rect)
        
        # Render the input box
        txt_surface = font.render(text, True, color)
        width = max(SCREEN_WIDTH // 2, txt_surface.get_width() + 10)
        input_box.w = width
        pygame.draw.rect(screen, color, input_box, 2)
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        
        # Render instructions
        instruction = font.render('Press ENTER to confirm', True, WHITE)
        instruction_rect = instruction.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5))
        screen.blit(instruction, instruction_rect)
        
        pygame.display.flip()
        clock.tick(30)
        
    return text.strip()

def show_level_selection(db_manager, user_id, max_level):
    """Show level selection screen"""
    selected_level = 1
    done = False
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_level = max(1, selected_level - 1)
                elif event.key == pygame.K_DOWN:
                    selected_level = min(max_level, selected_level + 1)
                elif event.key == pygame.K_RETURN:
                    done = True
                    
        screen.fill(BLACK)
        
        # Title
        title = large_font.render('Select Level', True, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(title, title_rect)
        
        # Level options
        for i in range(1, max_level + 1):
            color = GREEN if i == selected_level else WHITE
            difficulty = "Easy" if i == 1 else "Medium" if i == 2 else "Hard"
            level_text = font.render(f"Level {i} - {difficulty}", True, color)
            
            # Get high score for this level
            high_score = db_manager.get_high_score(user_id, i)
            score_text = font.render(f"High Score: {high_score}", True, color)
            
            level_rect = level_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + (i - 1) * 50))
            score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + (i - 1) * 50 + 25))
            
            screen.blit(level_text, level_rect)
            screen.blit(score_text, score_rect)
            
        # Instructions
        instruction = font.render('Use UP/DOWN arrows to select, ENTER to confirm', True, WHITE)
        instruction_rect = instruction.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.2))
        screen.blit(instruction, instruction_rect)
        
        pygame.display.flip()
        clock.tick(30)
        
    return selected_level

def show_game_over(score, restart_game):
    """Show game over screen and get player's choice"""
    done = False
    selection = 0  # 0 for restart, 1 for quit
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    selection = 1 - selection  # Toggle between restart and quit
                elif event.key == pygame.K_RETURN:
                    done = True
                    
        screen.fill(BLACK)
        
        # Game over message
        game_over_text = large_font.render('GAME OVER', True, RED)
        score_text = font.render(f'Your Score: {score}', True, WHITE)
        
        # Options
        restart_color = GREEN if selection == 0 else WHITE
        quit_color = GREEN if selection == 1 else WHITE
        
        restart_text = font.render('Restart Game', True, restart_color)
        quit_text = font.render('Quit', True, quit_color)
        
        # Position all text elements
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5))
        quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.3))
        
        screen.blit(game_over_text, game_over_rect)
        screen.blit(score_text, score_rect)
        screen.blit(restart_text, restart_rect)
        screen.blit(quit_text, quit_rect)
        
        pygame.display.flip()
        clock.tick(30)
    
    if selection == 0:
        restart_game()
    else:
        pygame.quit()
        sys.exit()

def main():
    # Initialize database manager
    db_manager = SnakeDbManager()
    
    # Get username from user
    username = get_username()
    
    # Check if user exists or create new user
    if db_manager.user_exists(username):
        user_id = db_manager.get_user_id(username)
        print(f"Welcome back, {username}!")
    else:
        user_id = db_manager.create_user(username)
        print(f"New user created: {username}")
    
    # Get the maximum level the user has access to (based on their progress)
    max_level = min(3, db_manager.get_user_level(user_id) + 1)
    
    def start_game():
        nonlocal max_level
        # Show level selection
        selected_level = show_level_selection(db_manager, user_id, max_level)
        
        # Initialize snake with selected level
        snake = Snake(level=selected_level)
        
        # Game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                if event.type == pygame.KEYDOWN:
                    pause_pressed = snake.handle_keys(event.key)
                    
                    # If pause key was pressed, save game state
                    if pause_pressed and not snake.game_over:
                        game_state = snake.to_dict()
                        db_manager.save_score(user_id, snake.score, snake.level, json.dumps(game_state))
                        
                        # Show pause message
                        pause_text = large_font.render('GAME PAUSED', True, WHITE)
                        save_text = font.render('Game state saved', True, WHITE)
                        continue_text = font.render('Press P to continue', True, WHITE)
                        
                        pause_rect = pause_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
                        save_rect = save_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                        continue_rect = continue_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5))
                        
                        screen.blit(pause_text, pause_rect)
                        screen.blit(save_text, save_rect)
                        screen.blit(continue_text, continue_rect)
                        pygame.display.update()
            
            if snake.game_over:
                # Save the score (game is over, no game state needed)
                db_manager.save_score(user_id, snake.score, snake.level)
                
                # If completed level successfully, unlock next level if available
                current_max_level = min(3, db_manager.get_user_level(user_id) + 1)
                if current_max_level > max_level:
                    max_level = current_max_level
                
                # Show game over screen
                show_game_over(snake.score, start_game)
                running = False
                continue
            
            # Fill the screen
            screen.fill(BLACK)
            
            # Move the snake (if not paused)
            snake.move()
            
            # Draw everything
            snake.draw(screen)
            
            # Draw score and level
            score_text = font.render(f'Score: {snake.score}', True, WHITE)
            level_text = font.render(f'Level: {snake.level}', True, WHITE)
            pause_info = font.render('Press P to pause and save', True, WHITE)
            
            screen.blit(score_text, (10, 10))
            screen.blit(level_text, (10, 40))
            screen.blit(pause_info, (SCREEN_WIDTH - pause_info.get_width() - 10, 10))
            
            # If game is paused, show message
            if snake.paused:
                pause_text = large_font.render('GAME PAUSED', True, WHITE)
                pause_rect = pause_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                screen.blit(pause_text, pause_rect)
            
            # Update the display
            pygame.display.update()
            
            # Set the game speed based on level
            clock.tick(SPEEDS[snake.level])
    
    try:
        start_game()
    finally:
        # Close the database connection when done
        db_manager.close_connection()
        pygame.quit()

if __name__ == "__main__":
    main() 
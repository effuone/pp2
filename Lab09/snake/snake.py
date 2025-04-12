import pygame
import random
import time
import sys
from pygame.locals import *

# Initialize pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game - Lab09')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

# Game settings
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE
FPS = 10  # Initial FPS (controls snake speed)

# Fonts
font = pygame.font.SysFont('Arial', 32)
small_font = pygame.font.SysFont('Arial', 24)

# Game variables
score = 0
level = 1

# Wall settings
walls = []

# Food timer constants
FOOD_TIMER_MAX = 15  # Food will disappear after 15 seconds
FOOD_WARNING_TIME = 5  # Start blinking when 5 seconds left

class Food:
    """
    Class to represent food with different types, values, and disappearing functionality
    """
    def __init__(self, snake_body):
        # Randomly determine food type
        self.food_type = random.choices(
            ['regular', 'bonus', 'special'],
            weights=[0.7, 0.2, 0.1],  # 70% regular, 20% bonus, 10% special
            k=1
        )[0]
        
        # Set food value and color based on type
        if self.food_type == 'regular':
            self.value = 1
            self.color = RED
        elif self.food_type == 'bonus':
            self.value = 2
            self.color = ORANGE
        else:  # special
            self.value = 5
            self.color = PURPLE
        
        # Generate position
        self.position = self.generate_position(snake_body)
        
        # Start the timer for this food
        self.timer = FOOD_TIMER_MAX
        self.visible = True  # Used for blinking effect
        self.elapsed_time = 0
    
    def generate_position(self, snake_body):
        """
        Generate a random position that is not on a wall or the snake
        """
        while True:
            pos = (random.randint(1, GRID_WIDTH - 2), random.randint(1, GRID_HEIGHT - 2))
            if pos not in walls and pos not in snake_body:
                return pos
    
    def update(self, delta_time):
        """
        Update the food's timer and visibility
        """
        self.elapsed_time += delta_time
        self.timer = max(0, FOOD_TIMER_MAX - self.elapsed_time)
        
        # If time is running out, make the food blink
        if self.timer <= FOOD_WARNING_TIME:
            # Blink faster as the timer gets closer to 0
            blink_rate = max(0.1, self.timer / FOOD_WARNING_TIME)
            if pygame.time.get_ticks() % int(1000 * blink_rate) < 500:
                self.visible = True
            else:
                self.visible = False
        else:
            self.visible = True
        
        return self.timer > 0  # Return whether the food is still valid
    
    def draw(self):
        """
        Draw the food on the screen if it's visible
        """
        if self.visible:
            # Draw different shapes based on food type
            if self.food_type == 'regular':
                # Regular food is a circle
                pygame.draw.circle(window, self.color, 
                                (self.position[0] * CELL_SIZE + CELL_SIZE // 2, 
                                 self.position[1] * CELL_SIZE + CELL_SIZE // 2), 
                                CELL_SIZE // 2 - 2)
            elif self.food_type == 'bonus':
                # Bonus food is a diamond
                center_x = self.position[0] * CELL_SIZE + CELL_SIZE // 2
                center_y = self.position[1] * CELL_SIZE + CELL_SIZE // 2
                size = CELL_SIZE // 2 - 2
                
                points = [
                    (center_x, center_y - size),  # Top
                    (center_x + size, center_y),  # Right
                    (center_x, center_y + size),  # Bottom
                    (center_x - size, center_y)   # Left
                ]
                
                pygame.draw.polygon(window, self.color, points)
            else:  # special
                # Special food is a star-like shape
                rect = pygame.Rect(
                    self.position[0] * CELL_SIZE + 2, 
                    self.position[1] * CELL_SIZE + 2, 
                    CELL_SIZE - 4, CELL_SIZE - 4
                )
                pygame.draw.rect(window, self.color, rect)
                
                # Add a highlight in the center
                pygame.draw.circle(window, YELLOW, 
                                (self.position[0] * CELL_SIZE + CELL_SIZE // 2, 
                                 self.position[1] * CELL_SIZE + CELL_SIZE // 2), 
                                CELL_SIZE // 4)
            
            # Display timer if it's getting low
            if self.timer <= FOOD_WARNING_TIME:
                # Show the timer count above the food
                timer_text = small_font.render(f"{int(self.timer)}", True, WHITE)
                window.blit(timer_text, 
                          (self.position[0] * CELL_SIZE - 5, 
                           self.position[1] * CELL_SIZE - 25))

def generate_walls():
    """
    Generate walls around the border and some obstacles in the playing area
    """
    global walls
    walls = []
    
    # Border walls
    for x in range(GRID_WIDTH):
        walls.append((x, 0))  # Top wall
        walls.append((x, GRID_HEIGHT-1))  # Bottom wall
    
    for y in range(GRID_HEIGHT):
        walls.append((0, y))  # Left wall
        walls.append((GRID_WIDTH-1, y))  # Right wall
    
    # Add some random obstacles based on the level
    if level >= 2:
        # Add some vertical obstacles
        for _ in range(level - 1):
            x = random.randint(5, GRID_WIDTH - 6)
            wall_length = random.randint(3, 8)
            y_start = random.randint(5, GRID_HEIGHT - wall_length - 5)
            
            for y in range(y_start, y_start + wall_length):
                walls.append((x, y))
    
    if level >= 3:
        # Add some horizontal obstacles
        for _ in range(level - 2):
            y = random.randint(5, GRID_HEIGHT - 6)
            wall_length = random.randint(3, 8)
            x_start = random.randint(5, GRID_WIDTH - wall_length - 5)
            
            for x in range(x_start, x_start + wall_length):
                walls.append((x, y))

def draw_grid():
    """
    Draw the grid on the window
    """
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(window, (50, 50, 50), (x, 0), (x, HEIGHT))
    
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(window, (50, 50, 50), (0, y), (WIDTH, y))

def draw_snake(snake_body):
    """
    Draw the snake on the window
    """
    for i, segment in enumerate(snake_body):
        # Draw the snake head in a different color
        if i == 0:
            pygame.draw.rect(window, GREEN, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            # Draw snake eyes
            eye_size = CELL_SIZE // 5
            pygame.draw.circle(window, BLACK, (segment[0] * CELL_SIZE + CELL_SIZE // 3, segment[1] * CELL_SIZE + CELL_SIZE // 3), eye_size)
            pygame.draw.circle(window, BLACK, (segment[0] * CELL_SIZE + 2 * CELL_SIZE // 3, segment[1] * CELL_SIZE + CELL_SIZE // 3), eye_size)
        else:
            # Draw the body segments with a slight gradient effect
            color_intensity = max(50, 200 - i * 5)
            pygame.draw.rect(window, (0, color_intensity, 0), (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_walls():
    """
    Draw the walls on the window
    """
    for wall in walls:
        pygame.draw.rect(window, BLUE, (wall[0] * CELL_SIZE, wall[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_score():
    """
    Draw the score and level information on the window
    """
    score_text = small_font.render(f'Score: {score}', True, WHITE)
    level_text = small_font.render(f'Level: {level}', True, WHITE)
    window.blit(score_text, (10, 10))
    window.blit(level_text, (WIDTH - 120, 10))

def show_game_over():
    """
    Show the game over screen
    """
    window.fill(BLACK)
    
    game_over_text = font.render('GAME OVER', True, RED)
    score_text = font.render(f'Final Score: {score}', True, WHITE)
    level_text = font.render(f'Final Level: {level}', True, WHITE)
    restart_text = font.render('Press R to restart', True, WHITE)
    quit_text = font.render('Press Q to quit', True, WHITE)
    
    window.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 3))
    window.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 3 + 50))
    window.blit(level_text, (WIDTH // 2 - level_text.get_width() // 2, HEIGHT // 3 + 100))
    window.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 3 + 170))
    window.blit(quit_text, (WIDTH // 2 - quit_text.get_width() // 2, HEIGHT // 3 + 220))
    
    pygame.display.flip()

def level_up():
    """
    Increase the level and adjust game parameters
    """
    global level, FPS
    level += 1
    FPS += 2  # Increase the game speed
    
    # Show level up message
    window.fill(BLACK)
    level_up_text = font.render(f'Level {level}!', True, YELLOW)
    speed_text = font.render('Speed increased!', True, YELLOW)
    continue_text = font.render('Press any key to continue', True, WHITE)
    
    window.blit(level_up_text, (WIDTH // 2 - level_up_text.get_width() // 2, HEIGHT // 3))
    window.blit(speed_text, (WIDTH // 2 - speed_text.get_width() // 2, HEIGHT // 3 + 50))
    window.blit(continue_text, (WIDTH // 2 - continue_text.get_width() // 2, HEIGHT // 3 + 120))
    
    pygame.display.flip()
    
    # Wait for key press
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                waiting = False
    
    # Generate new walls for the new level
    generate_walls()

def main_game():
    global score, level, FPS
    
    # Reset game variables
    score = 0
    level = 1
    FPS = 10
    
    # Generate walls
    generate_walls()
    
    # Initialize snake
    snake_x = GRID_WIDTH // 4
    snake_y = GRID_HEIGHT // 2
    snake_body = [(snake_x, snake_y), (snake_x - 1, snake_y), (snake_x - 2, snake_y)]
    
    # Set initial direction (right)
    direction = 'RIGHT'
    change_to = direction
    
    # Generate food
    food = Food(snake_body)
    
    # Food counter for level ups
    food_eaten = 0
    
    # Create clock
    clock = pygame.time.Clock()
    last_time = time.time()
    
    # Game loop
    game_active = True
    while game_active:
        current_time = time.time()
        delta_time = current_time - last_time
        last_time = current_time
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            # Store the direction based on key press
            elif event.type == KEYDOWN:
                if event.key == K_UP or event.key == K_w:
                    change_to = 'UP'
                elif event.key == K_DOWN or event.key == K_s:
                    change_to = 'DOWN'
                elif event.key == K_LEFT or event.key == K_a:
                    change_to = 'LEFT'
                elif event.key == K_RIGHT or event.key == K_d:
                    change_to = 'RIGHT'
        
        # Validate direction changes (prevent 180-degree turns)
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        elif change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        elif change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        elif change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
        
        # Move the snake based on direction
        if direction == 'UP':
            snake_y -= 1
        elif direction == 'DOWN':
            snake_y += 1
        elif direction == 'LEFT':
            snake_x -= 1
        elif direction == 'RIGHT':
            snake_x += 1
        
        # Check for collisions with walls or self
        if (snake_x, snake_y) in walls or (snake_x, snake_y) in snake_body:
            game_active = False
            show_game_over()
            break
        
        # Check for out of bounds (this is a backup check, as walls should prevent this)
        if snake_x < 0 or snake_x >= GRID_WIDTH or snake_y < 0 or snake_y >= GRID_HEIGHT:
            game_active = False
            show_game_over()
            break
        
        # Snake body growing mechanism
        snake_body.insert(0, (snake_x, snake_y))
        
        # Update food timer
        if not food.update(delta_time):
            # Food has expired, create a new one
            food = Food(snake_body)
        
        # Check if snake has eaten the food
        if snake_x == food.position[0] and snake_y == food.position[1]:
            # Increase score based on food value
            score += 10 * food.value
            
            # Increment food eaten counter
            food_eaten += food.value
            
            # Generate new food
            food = Food(snake_body)
            
            # Check for level up
            if food_eaten >= 3 + level:  # More food needed for higher levels
                food_eaten = 0
                level_up()
        else:
            # Remove the last segment if the snake didn't eat
            snake_body.pop()
        
        # Draw everything
        window.fill(BLACK)
        draw_grid()
        draw_walls()
        draw_snake(snake_body)
        food.draw()
        draw_score()
        
        # Update the display
        pygame.display.flip()
        
        # Control game speed
        clock.tick(FPS)
    
    # Game over loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_r:  # Restart
                    return main_game()
                elif event.key == K_q:  # Quit
                    pygame.quit()
                    sys.exit()

# Start the game
if __name__ == "__main__":
    main_game() 
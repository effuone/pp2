import pygame
import random
import time
import math
from pygame.locals import *

# Initialize pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Racer Game - Lab09')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GOLD = (255, 215, 0)
SILVER = (192, 192, 192)
BRONZE = (205, 127, 50)
GRAY = (128, 128, 128)

# Game settings
speed = 5
score = 0
coins_collected = 0
enemy_speed_increase_threshold = 5  # Number of coins needed to increase enemy speed
enemy_speed_increase_amount = 1      # How much to increase enemy speed
last_speed_increase = 0              # Track when we last increased speed

# Game clock
clock = pygame.time.Clock()
FPS = 60

# Font for text display
font = pygame.font.SysFont("Arial", 24)

class Player(pygame.sprite.Sprite):
    """
    Player class represents the car controlled by the user
    """
    def __init__(self):
        super().__init__()
        # Create a car-like rectangle for the player
        self.image = pygame.Surface((40, 70))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        
        # Position the player at the bottom center of the screen
        self.rect.center = (screen_width // 2, screen_height - 100)
        
        # Set initial movement speed
        self.speed = 5
    
    def update(self):
        """
        Update the player position based on keyboard input
        """
        # Get pressed keys
        keys = pygame.key.get_pressed()
        
        # Move the player based on arrow key inputs
        if keys[K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.bottom < screen_height:
            self.rect.y += self.speed

class Enemy(pygame.sprite.Sprite):
    """
    Enemy class represents the obstacles (other cars) that the player needs to avoid
    """
    def __init__(self, base_speed=None):
        super().__init__()
        # Create a car-like rectangle for the enemy
        self.image = pygame.Surface((40, 70))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        
        # Position the enemy randomly at the top of the screen
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(-200, -50)
        
        # Set initial movement speed (downward)
        self.base_speed = base_speed if base_speed else random.randint(4, 7)
        self.speed = self.base_speed
    
    def update(self):
        """
        Update the enemy position (moving downward)
        """
        # Move the enemy down
        self.rect.y += self.speed
        
        # If the enemy has moved off-screen, reset its position
        if self.rect.top > screen_height:
            self.rect.x = random.randint(0, screen_width - self.rect.width)
            self.rect.y = random.randint(-200, -50)
            self.speed = self.base_speed  # Reset to base speed when respawning
    
    def increase_speed(self, amount):
        """
        Increase the enemy's speed by the specified amount
        """
        self.base_speed += amount
        self.speed = self.base_speed

class Coin(pygame.sprite.Sprite):
    """
    Coin class represents collectible items that increase the player's score
    """
    def __init__(self):
        super().__init__()
        # Randomly determine coin type and value
        self.coin_type = random.choices(
            ['bronze', 'silver', 'gold'],
            weights=[0.6, 0.3, 0.1],  # 60% bronze, 30% silver, 10% gold
            k=1
        )[0]
        
        # Set coin value based on type
        if self.coin_type == 'bronze':
            self.value = 1
            self.color = BRONZE
            self.size = 18
        elif self.coin_type == 'silver':
            self.value = 2
            self.color = SILVER
            self.size = 20
        else:  # gold
            self.value = 5
            self.color = GOLD
            self.size = 22
        
        # Create a circular coin with appropriate color and size
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.size // 2, self.size // 2), self.size // 2)
        
        # Add detail to the coin to differentiate types
        if self.coin_type == 'bronze':
            pygame.draw.circle(self.image, (180, 100, 30), (self.size // 2, self.size // 2), self.size // 4)
        elif self.coin_type == 'silver':
            pygame.draw.circle(self.image, (160, 160, 160), (self.size // 2, self.size // 2), self.size // 4)
        else:  # gold
            pygame.draw.circle(self.image, (255, 180, 0), (self.size // 2, self.size // 2), self.size // 4)
        
        self.rect = self.image.get_rect()
        
        # Position the coin randomly on the screen
        self.rect.x = random.randint(50, screen_width - 50)
        self.rect.y = random.randint(-300, -50)
        
        # Set movement speed
        self.speed = random.randint(3, 6)
    
    def update(self):
        """
        Update the coin position (moving downward)
        """
        # Move the coin down
        self.rect.y += self.speed
        
        # If the coin has moved off-screen, reset its position
        if self.rect.top > screen_height:
            self.reset_position()
    
    def reset_position(self):
        """
        Reset the coin to a new random position above the screen and possibly change its type
        """
        # Potentially change coin type when reset
        self.coin_type = random.choices(
            ['bronze', 'silver', 'gold'],
            weights=[0.6, 0.3, 0.1],
            k=1
        )[0]
        
        # Update coin properties based on new type
        if self.coin_type == 'bronze':
            self.value = 1
            self.color = BRONZE
            self.size = 18
        elif self.coin_type == 'silver':
            self.value = 2
            self.color = SILVER
            self.size = 20
        else:  # gold
            self.value = 5
            self.color = GOLD
            self.size = 22
        
        # Update coin appearance
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.size // 2, self.size // 2), self.size // 2)
        
        # Add detail to the coin to differentiate types
        if self.coin_type == 'bronze':
            pygame.draw.circle(self.image, (180, 100, 30), (self.size // 2, self.size // 2), self.size // 4)
        elif self.coin_type == 'silver':
            pygame.draw.circle(self.image, (160, 160, 160), (self.size // 2, self.size // 2), self.size // 4)
        else:  # gold
            pygame.draw.circle(self.image, (255, 180, 0), (self.size // 2, self.size // 2), self.size // 4)
        
        self.rect = self.image.get_rect()
        
        # Reset position
        self.rect.x = random.randint(50, screen_width - 50)
        self.rect.y = random.randint(-300, -50)
        self.speed = random.randint(3, 6)

class Road:
    """
    Road class handles the drawing and movement of the road
    """
    def __init__(self):
        # Road parameters
        self.road_width = 300
        self.marking_width = 10
        self.marking_length = 50
        
        # Position parameters
        self.road_center = screen_width // 2
        self.left_edge = self.road_center - self.road_width // 2
        self.right_edge = self.road_center + self.road_width // 2
        
        # Marking parameters for animation
        self.markings_y = 0
    
    def update(self):
        """
        Update the road markings position for animation
        """
        # Move the markings down to create the illusion of movement
        self.markings_y += speed
        if self.markings_y >= screen_height:
            self.markings_y = 0
    
    def draw(self, surface):
        """
        Draw the road and markings on the given surface
        """
        # Draw the road
        pygame.draw.rect(surface, GRAY, (self.left_edge, 0, self.road_width, screen_height))
        
        # Draw the road edges
        pygame.draw.rect(surface, WHITE, (self.left_edge, 0, 5, screen_height))
        pygame.draw.rect(surface, WHITE, (self.right_edge - 5, 0, 5, screen_height))
        
        # Draw the center markings
        marking_start = -self.marking_length + (self.markings_y % (self.marking_length * 2))
        while marking_start < screen_height:
            pygame.draw.rect(surface, WHITE, 
                             (self.road_center - self.marking_width // 2, 
                              marking_start, self.marking_width, self.marking_length))
            marking_start += self.marking_length * 2

def show_score():
    """
    Display the player's score and collected coins
    """
    score_text = font.render(f"Score: {score}", True, WHITE)
    coins_text = font.render(f"Coins: {coins_collected}", True, YELLOW)
    
    # Also show the current enemy speed
    speed_text = font.render(f"Enemy Speed: {enemies.sprites()[0].base_speed:.1f}", True, WHITE)
    
    screen.blit(score_text, (10, 10))
    screen.blit(coins_text, (screen_width - 150, 10))
    screen.blit(speed_text, (10, 40))

def show_game_over():
    """
    Display the game over screen
    """
    game_over_text = font.render("GAME OVER", True, RED)
    score_text = font.render(f"Final Score: {score}", True, WHITE)
    coins_text = font.render(f"Coins Collected: {coins_collected}", True, YELLOW)
    restart_text = font.render("Press R to restart", True, WHITE)
    
    screen.blit(game_over_text, (screen_width // 2 - 80, screen_height // 2 - 60))
    screen.blit(score_text, (screen_width // 2 - 80, screen_height // 2 - 20))
    screen.blit(coins_text, (screen_width // 2 - 80, screen_height // 2 + 20))
    screen.blit(restart_text, (screen_width // 2 - 90, screen_height // 2 + 60))

def main_game():
    global speed, score, coins_collected, last_speed_increase
    
    # Reset game variables
    speed = 5
    score = 0
    coins_collected = 0
    last_speed_increase = 0
    
    # Create the player
    player = Player()
    player_group = pygame.sprite.Group()
    player_group.add(player)
    
    # Create enemies
    global enemies
    enemies = pygame.sprite.Group()
    for i in range(4):
        enemy = Enemy()
        enemies.add(enemy)
    
    # Create coins
    coins = pygame.sprite.Group()
    for i in range(3):
        coin = Coin()
        coins.add(coin)
    
    # Create the road
    road = Road()
    
    # Game state
    game_active = True
    
    # Main game loop
    while True:
        # Process events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == KEYDOWN:
                if event.key == K_r and not game_active:
                    # Restart the game
                    return main_game()
        
        # Update game if active
        if game_active:
            # Update road
            road.update()
            
            # Update player
            player_group.update()
            
            # Update enemies
            enemies.update()
            
            # Update coins
            coins.update()
            
            # Increment score
            score += 1
            
            # Check for collision with enemies
            if pygame.sprite.spritecollide(player, enemies, False):
                game_active = False
            
            # Check for collision with coins
            collected_coins = pygame.sprite.spritecollide(player, coins, False)
            for coin in collected_coins:
                coin.reset_position()
                coins_collected += coin.value
                score += coin.value * 100  # Bonus points based on coin value
                
                # Check if we need to increase enemy speed
                coins_since_last_increase = coins_collected - last_speed_increase
                if coins_since_last_increase >= enemy_speed_increase_threshold:
                    last_speed_increase = coins_collected
                    # Increase the speed of all enemies
                    for enemy in enemies:
                        enemy.increase_speed(enemy_speed_increase_amount)
                    
                    # Display a message about the speed increase
                    speed_up_text = font.render("Enemies Speed Up!", True, RED)
                    screen.blit(speed_up_text, (screen_width // 2 - 100, screen_height // 2))
                    pygame.display.flip()
                    # Brief pause to notice the speed increase
                    pygame.time.delay(500)
        
        # Draw everything
        screen.fill(BLACK)
        road.draw(screen)
        
        if game_active:
            # Draw player, enemies, and coins
            player_group.draw(screen)
            enemies.draw(screen)
            coins.draw(screen)
            
            # Show score
            show_score()
        else:
            # Show game over screen
            show_game_over()
        
        # Update the display
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick(FPS)

# Start the game
if __name__ == "__main__":
    main_game()
    pygame.quit() 
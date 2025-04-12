import pygame
import sys
import os
import math
import time
from datetime import datetime
from pygame.locals import *

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lab07: Pygame Application")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Fonts
font = pygame.font.SysFont('Arial', 24)

# Paths for assets
current_dir = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(current_dir, 'assets', 'images')
sound_dir = os.path.join(current_dir, 'assets', 'sounds')

# Music playlist
music_files = [os.path.join(sound_dir, f) for f in os.listdir(sound_dir) if f.endswith('.mp3')]
music_files.sort()  # Sort files for consistent ordering
current_song_index = 0

# Load music if files exist
if music_files:
    pygame.mixer.music.load(music_files[current_song_index])
else:
    print("No music files found in assets/sounds directory")

# Music player state
is_playing = False
song_names = [os.path.basename(file) for file in music_files]

# Ball properties
ball_radius = 25
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_speed = 20

# Create clock images for Mickey Clock
# Create a simple clock face
clock_center = (WIDTH // 4, HEIGHT // 2)
clock_radius = 100

# Create minute and second hands
minute_hand_length = 80
second_hand_length = 90

def draw_mickey_clock():
    # Draw clock face
    pygame.draw.circle(screen, WHITE, clock_center, clock_radius)
    pygame.draw.circle(screen, BLACK, clock_center, clock_radius, 2)
    
    # Draw Mickey's head
    pygame.draw.circle(screen, BLACK, clock_center, clock_radius - 5)
    
    # Draw Mickey's ears
    ear_radius = clock_radius // 2
    ear_offset = ear_radius + 10
    pygame.draw.circle(screen, BLACK, (clock_center[0] - ear_offset, clock_center[1] - ear_offset), ear_radius)
    pygame.draw.circle(screen, BLACK, (clock_center[0] + ear_offset, clock_center[1] - ear_offset), ear_radius)
    
    # Get current time
    now = datetime.now()
    minutes = now.minute
    seconds = now.second
    
    # Calculate angles
    minute_angle = math.radians(minutes * 6 - 90)  # 6 degrees per minute, -90 to adjust for pygame coordinate system
    second_angle = math.radians(seconds * 6 - 90)  # 6 degrees per second, -90 to adjust for pygame coordinate system
    
    # Draw minute hand (right hand)
    minute_x = clock_center[0] + minute_hand_length * math.cos(minute_angle)
    minute_y = clock_center[1] + minute_hand_length * math.sin(minute_angle)
    pygame.draw.line(screen, WHITE, clock_center, (minute_x, minute_y), 6)
    
    # Draw second hand (left hand)
    second_x = clock_center[0] + second_hand_length * math.cos(second_angle)
    second_y = clock_center[1] + second_hand_length * math.sin(second_angle)
    pygame.draw.line(screen, RED, clock_center, (second_x, second_y), 3)
    
    # Draw center dot
    pygame.draw.circle(screen, WHITE, clock_center, 8)

def draw_music_player():
    # Draw music player background
    player_rect = pygame.Rect(WIDTH // 2, 50, WIDTH // 2 - 20, HEIGHT // 3)
    pygame.draw.rect(screen, (50, 50, 50), player_rect)
    
    # Draw music player title
    title_text = font.render("Music Player", True, WHITE)
    screen.blit(title_text, (WIDTH // 2 + 10, 60))
    
    # Draw current song name
    if music_files:
        song_text = font.render(song_names[current_song_index], True, WHITE)
        screen.blit(song_text, (WIDTH // 2 + 10, 100))
    
    # Draw music player status
    status = "Playing" if is_playing else "Paused"
    status_text = font.render(f"Status: {status}", True, WHITE)
    screen.blit(status_text, (WIDTH // 2 + 10, 140))
    
    # Draw controls
    controls_text = font.render("Controls: SPACE (Play/Pause), N (Next), P (Previous)", True, WHITE)
    screen.blit(controls_text, (WIDTH // 2 + 10, 180))

def draw_ball_game():
    # Draw ball game area
    game_rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, WIDTH // 2 - 20, HEIGHT // 2 - 20)
    pygame.draw.rect(screen, (200, 200, 200), game_rect)
    
    # Draw game title
    title_text = font.render("Ball Game", True, BLACK)
    screen.blit(title_text, (WIDTH // 2 + 10, HEIGHT // 2 + 10))
    
    # Draw ball
    pygame.draw.circle(screen, RED, ball_pos, ball_radius)
    
    # Draw instructions
    controls_text = font.render("Use arrow keys to move the ball", True, BLACK)
    screen.blit(controls_text, (WIDTH // 2 + 10, HEIGHT - 50))

def play_next_song():
    global current_song_index
    if music_files:
        current_song_index = (current_song_index + 1) % len(music_files)
        pygame.mixer.music.load(music_files[current_song_index])
        if is_playing:
            pygame.mixer.music.play()

def play_previous_song():
    global current_song_index
    if music_files:
        current_song_index = (current_song_index - 1) % len(music_files)
        pygame.mixer.music.load(music_files[current_song_index])
        if is_playing:
            pygame.mixer.music.play()

def toggle_play_pause():
    global is_playing
    if music_files:
        if is_playing:
            pygame.mixer.music.pause()
            is_playing = False
        else:
            pygame.mixer.music.play()
            is_playing = True

def move_ball(key):
    # Check arrow key presses and move ball
    if key == K_UP and ball_pos[1] - ball_speed >= HEIGHT // 2 + ball_radius:
        ball_pos[1] -= ball_speed
    elif key == K_DOWN and ball_pos[1] + ball_speed <= HEIGHT - ball_radius - 20:
        ball_pos[1] += ball_speed
    elif key == K_LEFT and ball_pos[0] - ball_speed >= WIDTH // 2 + ball_radius:
        ball_pos[0] -= ball_speed
    elif key == K_RIGHT and ball_pos[0] + ball_speed <= WIDTH - ball_radius - 20:
        ball_pos[0] += ball_speed

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            # Music player controls
            if event.key == K_SPACE:
                toggle_play_pause()
            elif event.key == K_n:
                play_next_song()
            elif event.key == K_p:
                play_previous_song()
            # Ball game controls
            elif event.key in (K_UP, K_DOWN, K_LEFT, K_RIGHT):
                move_ball(event.key)
    
    # Clear screen
    screen.fill(BLACK)
    
    # Draw applications
    draw_mickey_clock()
    draw_music_player()
    draw_ball_game()
    
    # Update display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()

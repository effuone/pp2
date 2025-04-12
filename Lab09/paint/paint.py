import pygame
import sys
import math
from pygame.locals import *

# Initialize pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Paint Application - Lab09')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
BROWN = (165, 42, 42)

# List of available colors for the color palette
COLORS = [BLACK, WHITE, RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, ORANGE, PURPLE, BROWN]

# Drawing properties
current_color = BLACK
background_color = WHITE
brush_size = 5
drawing = False

# Current drawing tool
# Options: 'pencil', 'rectangle', 'circle', 'eraser', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus'
current_tool = 'pencil'

# Font
font = pygame.font.SysFont('Arial', 16)

# Start positions for shapes
start_pos = None

def draw_color_palette():
    """
    Draw the color palette on the screen
    """
    palette_width = 30
    palette_height = 30
    margin = 5
    x_start = 10
    y_start = 10
    
    # Draw color selection area
    pygame.draw.rect(screen, (200, 200, 200), (5, 5, 
                    len(COLORS) * (palette_width + margin) + margin, 
                    palette_height + 2 * margin))
    
    # Draw each color button
    for i, color in enumerate(COLORS):
        rect = pygame.Rect(x_start + i * (palette_width + margin), 
                          y_start, palette_width, palette_height)
        pygame.draw.rect(screen, color, rect)
        
        # Draw a border around the currently selected color
        if color == current_color:
            pygame.draw.rect(screen, BLACK, rect, 2)

def draw_tools_palette():
    """
    Draw the tools palette on the screen
    """
    tools_start_x = 10
    tools_start_y = 60
    tool_width = 120
    tool_height = 25
    margin = 5
    
    tools = [
        ('Pencil', 'pencil'), 
        ('Rectangle', 'rectangle'), 
        ('Circle', 'circle'), 
        ('Square', 'square'),
        ('Right Triangle', 'right_triangle'),
        ('Equi Triangle', 'equilateral_triangle'),
        ('Rhombus', 'rhombus'),
        ('Eraser', 'eraser')
    ]
    
    # Draw tools selection area
    pygame.draw.rect(screen, (200, 200, 200), 
                    (5, tools_start_y - 5, 
                     tool_width + 2 * margin, 
                     len(tools) * (tool_height + margin) + margin))
    
    # Draw each tool button
    for i, (tool_name, tool_id) in enumerate(tools):
        rect = pygame.Rect(tools_start_x, 
                          tools_start_y + i * (tool_height + margin), 
                          tool_width, tool_height)
        
        # Highlight the current tool
        if tool_id == current_tool:
            pygame.draw.rect(screen, (150, 150, 255), rect)
        else:
            pygame.draw.rect(screen, (220, 220, 220), rect)
        
        # Draw tool name
        text = font.render(tool_name, True, BLACK)
        screen.blit(text, (rect.x + 5, rect.y + 5))
        
        # Draw border
        pygame.draw.rect(screen, BLACK, rect, 1)

def draw_brush_size_control():
    """
    Draw the brush size control on the screen
    """
    start_x = 10
    start_y = 320
    width = 80
    height = 30
    margin = 5
    
    # Draw brush size control area
    pygame.draw.rect(screen, (200, 200, 200), 
                    (5, start_y - 5, 
                     width + 2 * margin, 
                     2 * (height + margin) + margin))
    
    # Draw brush size label
    text = font.render(f"Brush Size: {brush_size}", True, BLACK)
    screen.blit(text, (start_x, start_y))
    
    # Draw increase button
    increase_rect = pygame.Rect(start_x, start_y + height + margin, width // 2 - 5, height)
    pygame.draw.rect(screen, (220, 220, 220), increase_rect)
    pygame.draw.rect(screen, BLACK, increase_rect, 1)
    text = font.render("+", True, BLACK)
    screen.blit(text, (increase_rect.x + increase_rect.width // 2 - 4, increase_rect.y + 5))
    
    # Draw decrease button
    decrease_rect = pygame.Rect(start_x + width // 2 + 5, start_y + height + margin, width // 2 - 5, height)
    pygame.draw.rect(screen, (220, 220, 220), decrease_rect)
    pygame.draw.rect(screen, BLACK, decrease_rect, 1)
    text = font.render("-", True, BLACK)
    screen.blit(text, (decrease_rect.x + decrease_rect.width // 2 - 4, decrease_rect.y + 5))
    
    return increase_rect, decrease_rect

def check_color_selection(pos):
    """
    Check if a color was selected from the palette
    """
    global current_color
    
    palette_width = 30
    palette_height = 30
    margin = 5
    x_start = 10
    y_start = 10
    
    for i, color in enumerate(COLORS):
        rect = pygame.Rect(x_start + i * (palette_width + margin), 
                          y_start, palette_width, palette_height)
        if rect.collidepoint(pos):
            current_color = color
            return True
    
    return False

def check_tool_selection(pos):
    """
    Check if a tool was selected from the toolbar
    """
    global current_tool
    
    tools_start_x = 10
    tools_start_y = 60
    tool_width = 120
    tool_height = 25
    margin = 5
    
    tools = [
        ('Pencil', 'pencil'), 
        ('Rectangle', 'rectangle'), 
        ('Circle', 'circle'), 
        ('Square', 'square'),
        ('Right Triangle', 'right_triangle'),
        ('Equi Triangle', 'equilateral_triangle'),
        ('Rhombus', 'rhombus'),
        ('Eraser', 'eraser')
    ]
    
    for i, (_, tool_id) in enumerate(tools):
        rect = pygame.Rect(tools_start_x, 
                          tools_start_y + i * (tool_height + margin), 
                          tool_width, tool_height)
        if rect.collidepoint(pos):
            current_tool = tool_id
            return True
    
    return False

def check_brush_size_control(pos, increase_rect, decrease_rect):
    """
    Check if a brush size control was clicked
    """
    global brush_size
    
    if increase_rect.collidepoint(pos):
        brush_size = min(50, brush_size + 1)
        return True
    elif decrease_rect.collidepoint(pos):
        brush_size = max(1, brush_size - 1)
        return True
    
    return False

def draw_pencil(screen, color, start_pos, end_pos, size):
    """
    Draw a line between two points for pencil tool
    """
    pygame.draw.line(screen, color, start_pos, end_pos, size)
    # Draw a circle at the end point to make the line smoother
    pygame.draw.circle(screen, color, end_pos, size // 2)

def draw_rectangle(screen, color, start_pos, end_pos, size):
    """
    Draw a rectangle with the given start and end positions
    """
    x = min(start_pos[0], end_pos[0])
    y = min(start_pos[1], end_pos[1])
    width = abs(start_pos[0] - end_pos[0])
    height = abs(start_pos[1] - end_pos[1])
    
    pygame.draw.rect(screen, color, (x, y, width, height), size)

def draw_square(screen, color, start_pos, end_pos, size):
    """
    Draw a square based on the start and end positions
    The side length is determined by the maximum of width and height
    """
    # Determine the side length
    side_length = max(abs(start_pos[0] - end_pos[0]), abs(start_pos[1] - end_pos[1]))
    
    # Calculate the top-left corner position
    if end_pos[0] >= start_pos[0]:  # Moving right
        x = start_pos[0]
    else:  # Moving left
        x = start_pos[0] - side_length
    
    if end_pos[1] >= start_pos[1]:  # Moving down
        y = start_pos[1]
    else:  # Moving up
        y = start_pos[1] - side_length
    
    pygame.draw.rect(screen, color, (x, y, side_length, side_length), size)

def draw_circle(screen, color, start_pos, end_pos, size):
    """
    Draw a circle with the center at start_pos and radius to end_pos
    """
    radius = int(math.sqrt((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2))
    pygame.draw.circle(screen, color, start_pos, radius, size)

def draw_right_triangle(screen, color, start_pos, end_pos, size):
    """
    Draw a right triangle with one vertex at start_pos and the right angle at end_pos
    """
    # The three points of the triangle
    p1 = start_pos  # First point (top/start)
    p2 = (end_pos[0], start_pos[1])  # Second point (top-right)
    p3 = end_pos  # Third point (bottom-right)
    
    # Draw the three sides
    pygame.draw.line(screen, color, p1, p2, size)
    pygame.draw.line(screen, color, p2, p3, size)
    pygame.draw.line(screen, color, p3, p1, size)

def draw_equilateral_triangle(screen, color, start_pos, end_pos, size):
    """
    Draw an equilateral triangle with the first vertex at start_pos and the second at end_pos
    """
    # Calculate the distance between the first two points
    dx = end_pos[0] - start_pos[0]
    dy = end_pos[1] - start_pos[1]
    distance = math.sqrt(dx**2 + dy**2)
    
    # Calculate the angle
    angle = math.atan2(dy, dx)
    
    # For an equilateral triangle, the third point is at angle + 120 degrees
    third_angle = angle + (2 * math.pi / 3)
    
    # Calculate the third point
    third_x = start_pos[0] + distance * math.cos(third_angle)
    third_y = start_pos[1] + distance * math.sin(third_angle)
    
    # Draw the three sides
    pygame.draw.line(screen, color, start_pos, end_pos, size)
    pygame.draw.line(screen, color, end_pos, (third_x, third_y), size)
    pygame.draw.line(screen, color, (third_x, third_y), start_pos, size)

def draw_rhombus(screen, color, start_pos, end_pos, size):
    """
    Draw a rhombus with the first diagonal from start_pos to end_pos
    """
    # Calculate the midpoint of the first diagonal
    mid_x = (start_pos[0] + end_pos[0]) // 2
    mid_y = (start_pos[1] + end_pos[1]) // 2
    
    # Calculate half of the first diagonal length
    d1_half = math.sqrt((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2) / 2
    
    # Calculate the direction vector of the first diagonal
    dx = end_pos[0] - start_pos[0]
    dy = end_pos[1] - start_pos[1]
    
    # Rotate 90 degrees to get the direction of the second diagonal
    # Second diagonal is perpendicular to the first diagonal
    d2_dx = -dy
    d2_dy = dx
    
    # Normalize the direction vector
    length = math.sqrt(d2_dx**2 + d2_dy**2)
    if length > 0:
        d2_dx = d2_dx / length
        d2_dy = d2_dy / length
    
    # Calculate points of the second diagonal
    half_length = d1_half / 2  # Adjust this factor to control rhombus shape
    p3_x = int(mid_x + half_length * d2_dx)
    p3_y = int(mid_y + half_length * d2_dy)
    p4_x = int(mid_x - half_length * d2_dx)
    p4_y = int(mid_y - half_length * d2_dy)
    
    # Draw the rhombus
    points = [start_pos, (p3_x, p3_y), end_pos, (p4_x, p4_y)]
    pygame.draw.polygon(screen, color, points, size)

def use_eraser(screen, pos, size):
    """
    Erase at the given position by drawing with the background color
    """
    pygame.draw.circle(screen, background_color, pos, size)

def draw_shape_preview(screen, tool, start_pos, current_pos):
    """
    Draw a preview of the shape being drawn
    """
    if tool == 'rectangle':
        # Create a temporary surface for preview
        preview_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        preview_surface.fill((0, 0, 0, 0))  # Transparent
        draw_rectangle(preview_surface, (*current_color, 128), start_pos, current_pos, brush_size)
        screen.blit(preview_surface, (0, 0))
    
    elif tool == 'circle':
        preview_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        preview_surface.fill((0, 0, 0, 0))
        draw_circle(preview_surface, (*current_color, 128), start_pos, current_pos, brush_size)
        screen.blit(preview_surface, (0, 0))
    
    elif tool == 'square':
        preview_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        preview_surface.fill((0, 0, 0, 0))
        draw_square(preview_surface, (*current_color, 128), start_pos, current_pos, brush_size)
        screen.blit(preview_surface, (0, 0))
    
    elif tool == 'right_triangle':
        preview_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        preview_surface.fill((0, 0, 0, 0))
        draw_right_triangle(preview_surface, (*current_color, 128), start_pos, current_pos, brush_size)
        screen.blit(preview_surface, (0, 0))
    
    elif tool == 'equilateral_triangle':
        preview_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        preview_surface.fill((0, 0, 0, 0))
        draw_equilateral_triangle(preview_surface, (*current_color, 128), start_pos, current_pos, brush_size)
        screen.blit(preview_surface, (0, 0))
    
    elif tool == 'rhombus':
        preview_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        preview_surface.fill((0, 0, 0, 0))
        draw_rhombus(preview_surface, (*current_color, 128), start_pos, current_pos, brush_size)
        screen.blit(preview_surface, (0, 0))

def main():
    global drawing, start_pos, current_color, current_tool, brush_size
    
    # Create a drawing canvas
    canvas = pygame.Surface((WIDTH, HEIGHT))
    canvas.fill(background_color)
    
    # Main loop
    running = True
    clock = pygame.time.Clock()
    
    while running:
        # Get mouse position
        pos = pygame.mouse.get_pos()
        
        # Draw the canvas and UI
        screen.blit(canvas, (0, 0))
        draw_color_palette()
        draw_tools_palette()
        increase_rect, decrease_rect = draw_brush_size_control()
        
        # Show current tool and color
        info_text = font.render(f"Tool: {current_tool.replace('_', ' ').capitalize()}", True, BLACK)
        screen.blit(info_text, (10, 400))
        
        # Draw a preview of the brush
        if current_tool == 'pencil' or current_tool == 'eraser':
            # Don't show the brush preview in the UI area
            if pos[1] > 450:
                if current_tool == 'eraser':
                    pygame.draw.circle(screen, BLACK, pos, brush_size, 1)
                else:
                    pygame.draw.circle(screen, current_color, pos, brush_size // 2)
        
        # Draw shape preview if we're currently drawing a shape
        if drawing and current_tool not in ['pencil', 'eraser']:
            draw_shape_preview(screen, current_tool, start_pos, pos)
        
        # Process events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            
            elif event.type == MOUSEBUTTONDOWN:
                # Check if UI elements were clicked
                if check_color_selection(pos):
                    continue
                if check_tool_selection(pos):
                    continue
                if check_brush_size_control(pos, increase_rect, decrease_rect):
                    continue
                
                # Start drawing
                drawing = True
                start_pos = pos
                
                # For pencil and eraser, draw immediately
                if current_tool == 'pencil':
                    draw_pencil(canvas, current_color, pos, pos, brush_size)
                elif current_tool == 'eraser':
                    use_eraser(canvas, pos, brush_size)
            
            elif event.type == MOUSEMOTION:
                if drawing:
                    if current_tool == 'pencil':
                        draw_pencil(canvas, current_color, start_pos, pos, brush_size)
                        start_pos = pos
                    elif current_tool == 'eraser':
                        use_eraser(canvas, pos, brush_size)
            
            elif event.type == MOUSEBUTTONUP:
                if drawing:
                    drawing = False
                    
                    # Draw shapes when mouse is released
                    if current_tool == 'rectangle':
                        draw_rectangle(canvas, current_color, start_pos, pos, brush_size)
                    elif current_tool == 'circle':
                        draw_circle(canvas, current_color, start_pos, pos, brush_size)
                    elif current_tool == 'square':
                        draw_square(canvas, current_color, start_pos, pos, brush_size)
                    elif current_tool == 'right_triangle':
                        draw_right_triangle(canvas, current_color, start_pos, pos, brush_size)
                    elif current_tool == 'equilateral_triangle':
                        draw_equilateral_triangle(canvas, current_color, start_pos, pos, brush_size)
                    elif current_tool == 'rhombus':
                        draw_rhombus(canvas, current_color, start_pos, pos, brush_size)
            
            elif event.type == KEYDOWN:
                # Clear the canvas with C key
                if event.key == K_c:
                    canvas.fill(background_color)
                # Save the canvas with S key
                elif event.key == K_s:
                    pygame.image.save(canvas, "painting.png")
                    print("Painting saved as painting.png")
        
        # Update the display
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main() 
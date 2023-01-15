import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen size and caption
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Snake Game")

# Set colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set snake block size
block_size = 10

# Set snake starting position
snake_x = 150
snake_y = 150

# Set food position
foodx = 0
foody = 0

# Set snake movement speed
snake_speed = 10

# Set snake direction
snake_direction = "right"

# Create game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle snake movement
    if snake_direction == "right":
        snake_x += snake_speed
    elif snake_direction == "left":
        snake_x -= snake_speed
    elif snake_direction == "up":
        snake_y -= snake_speed
    elif snake_direction == "down":
        snake_y += snake_speed

    # Handle food spawning
    if foodx == 0 and foody == 0:
        foodx = random.randint(0, 390)
        foody = random.randint(0, 290)

    # Handle snake collision with food
    if snake_x == foodx and snake_y == foody:
        foodx = 0
        foody = 0

    # Handle snake collision with screen edges
    if snake_x >= 400 or snake_x < 0 or snake_y >= 300 or snake_y < 0:
        running = False

    # Clear screen
    screen.fill(white)

    # Draw snake
    pygame.draw.rect(screen, black, [snake_x, snake_y, block_size, block_size])

    # Draw food
    pygame.draw.rect(screen, red, [foodx, foody, block_size, block_size])

    # Update display
    pygame.display.update()

# Quit Pygame
pygame.quit()

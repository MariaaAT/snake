import pygame


# Initialize Pygame
pygame.init()

# Set the window dimensions
width, height = 640, 480

# Create the window
screen = pygame.display.set_mode((width, height))

field_size = 20, 14
block_w = width/field_size[0]
block_h = height/field_size[1]

# snake
snake = [(3, 3), (2, 3), (2, 2), (2, 1)]

# Set the rectangle color to red
color = (255, 0, 0)
color_head = (0, 255, 0)

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

dir = (1, 0)

# Run the Pygame loop
running = True
while running:
    # Moving the snake down
    snake = [(snake[0][0] + dir[0], snake[0][1] + dir[1])] + snake[:-1]

    # Set the background color to white
    screen.fill((255, 255, 255))

    # Draw the snake
    pygame.draw.rect(screen, color_head, pygame.Rect(snake[0][1] * block_h, snake[0][0] * block_w, block_h, block_w))
    for block in snake[1:]:
        pygame.draw.rect(screen, color, pygame.Rect(block[1] * block_h, block[0] * block_w, block_h, block_w))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the window display
    pygame.display.flip()

    clock.tick(1)

# Quit Pygame
pygame.quit()
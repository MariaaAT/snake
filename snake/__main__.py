import pygame


# Initialize Pygame
pygame.init()

# Set the window dimensions
width, height = 640, 480

# Create the window
screen = pygame.display.set_mode((width, height))

# Set the background color to white
screen.fill((255, 255, 255))

field_size = 20, 14
block_w = width/field_size[0]
block_h = height/field_size[1]

# snake
snake = [(3, 3), (2, 3), (2, 2), (2, 1)]

# Set the rectangle color to red
color = (255, 0, 0)
color_head = (0, 255, 0)

# Draw the snake
pygame.draw.rect(screen, color_head, pygame.Rect(snake[0][1] * block_h, snake[0][0] * block_w, block_h, block_w))
for block in snake[1:]:
    pygame.draw.rect(screen, color, pygame.Rect(block[1] * block_h, block[0] * block_w, block_h, block_w))

# Update the window display
pygame.display.flip()

# Run the Pygame loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
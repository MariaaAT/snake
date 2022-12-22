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
block = (3, 2)

# Set the rectangle color to red
color = (255, 0, 0)

# Draw a rectangle at position (50, 50) with size (100, 50)
pygame.draw.rect(screen, color, pygame.Rect(block[0]*block_w, block[1]*block_h, block_w, block_h))

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
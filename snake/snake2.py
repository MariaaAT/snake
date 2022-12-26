import pygame

# Initialise the game
pygame.init()

# Set the window dimensions
# Create window
width, height = 680, 480
background_colour = (255, 255, 255)
screen = pygame.display.set_mode((width, height))  # This actually created the window

field_size = 20, 14

# Create blocks and snake
block_w = width // field_size[0]
block_h = height // field_size[1]
snake = [(3, 3), (3, 2), (3, 1)]
colour_head = (43, 132, 0)
colour = (0, 255, 117)

# Create a clock object to slow down the amount of frame rates per second
clock = pygame.time.Clock()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_colour)  # Fill the window with a background colour

    pygame.draw.rect(screen, colour_head, pygame.Rect(snake[0][0] * block_w, snake[0][1] * block_h, block_w, block_h))
    for block in snake[1:]:
        pygame.draw.rect(screen, colour,
                         pygame.Rect(block[0] * block_w, block[1] * block_h, block_w, block_h))

    pygame.display.flip()  # Update the window display

    clock.tick(60)


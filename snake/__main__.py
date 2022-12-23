import random
import pygame

# Initialize Pygame
pygame.init()

# Set the window dimensions
width, height = 640, 480

# Create the window
screen = pygame.display.set_mode((width, height))

field_size = 20, 14
block_w = width // field_size[0]
block_h = height // field_size[1]

# snake
snake = [(3, 3), (2, 3), (2, 2), (2, 1)]

# Set the rectangle color to red
color = (255, 0, 0)
color_head = (0, 255, 0)

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

dir = (1, 0)
# Set the treat variable outside the loop so the timer doesn't affect this variable
treat = (random.randint(0, field_size[0] - 1), random.randint(0, field_size[1] - 1))

MOVE_EVENT = pygame.USEREVENT + 1
pygame.event.post(pygame.event.Event(MOVE_EVENT))

# Run the Pygame loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == MOVE_EVENT:
            # Remember snake end
            snake_end = snake[-1]

            # Moving the snake down
            snake = [((snake[0][0] + dir[0]) % field_size[0], (snake[0][1] + dir[1]) % field_size[1])] + snake[:-1]

            # Check if snake ate the treat
            if snake[0] == treat:
                snake.append(snake_end)
                treat = (random.randint(0, field_size[0] - 1), random.randint(0, field_size[1] - 1))
                print(treat)

            pygame.time.set_timer(pygame.event.Event(MOVE_EVENT), 250)

        if event.type == pygame.QUIT:
            running = False

    # Get the state of the keyboard keys
    keys = pygame.key.get_pressed()

    # Change direction if arrow keys pressed
    if keys[pygame.K_DOWN] and dir != (0, -1):
        dir = (0, 1)
    elif keys[pygame.K_UP] and dir != (0, 1):
        dir = (0, -1)
    elif keys[pygame.K_LEFT] and dir != (1, 0):
        dir = (-1, 0)
    elif keys[pygame.K_RIGHT] and dir != (-1, 0):
        dir = (1, 0)

    # Set the background color to white
    screen.fill((255, 255, 255))

    # Add a block in random position (treat)
    pygame.draw.rect(screen, color, pygame.Rect(treat[0] * block_w, treat[1] * block_h, block_w, block_h))

    # Draw the snake
    pygame.draw.rect(screen, color_head,
                     pygame.Rect(snake[0][0] * block_w, snake[0][1] * block_h, block_w, block_h))
    for block in snake[1:]:
        pygame.draw.rect(screen, color, pygame.Rect(block[0] * block_w, block[1] * block_h, block_w, block_h))

    # Update the window display
    pygame.display.flip()

    clock.tick(60)

# Quit Pygame
pygame.quit()
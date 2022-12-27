import pygame
import random

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

# Set the direction
dir = (0, 1)

# Set a move event
MOVE_EVENT = pygame.USEREVENT + 1
#pygame.event.post(pygame.event.Event(MOVE_EVENT)) # post makes the event happen inmediately
pygame.time.set_timer(pygame.event.Event(MOVE_EVENT), 1) # The number says how much time passes until the event happens

treat = (random.randint(0, field_size[0] - 1), random.randint(0, field_size[1] - 1))

running = True
while running:
    for event in pygame.event.get():  # This pulls event from the event database, afterwards there's no more events in there
        if event.type == pygame.QUIT:
            running = False

        # Move the snake
        if event.type == MOVE_EVENT:
            snake = [((snake[0][0] + dir[0]) % field_size[0], (snake[0][1] + dir[1]) % field_size[1])] + snake[:-1]

            end_snake = snake[-1]
            if treat == snake[0]:
                snake.append(end_snake)
                treat = (random.randint(0, field_size[0] - 1), random.randint(0, field_size[1] - 1))

            pygame.time.set_timer(pygame.event.Event(MOVE_EVENT), 500)

    # Move the snake with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and dir != (0, 1):
        dir = (0, -1)
    if keys[pygame.K_DOWN] and dir != (0, -1):
        dir = (0, 1)
    if keys[pygame.K_RIGHT] and dir != (-1, 0):
        dir = (1, 0)
    if keys[pygame.K_LEFT] and dir != (1, 0):
        dir = (-1, 0)

    screen.fill(background_colour)  # Fill the window with a background colour

    # Draw the treat
    pygame.draw.rect(screen, colour, pygame.Rect(treat[0] * block_w, treat[1] * block_h, block_w, block_h))

    pygame.draw.rect(screen, colour_head, pygame.Rect(snake[0][0] * block_w, snake[0][1] * block_h, block_w, block_h))
    for block in snake[1:]:
        pygame.draw.rect(screen, colour,
                         pygame.Rect(block[0] * block_w, block[1] * block_h, block_w, block_h))

    pygame.display.flip()  # Update the window display

    clock.tick(60)


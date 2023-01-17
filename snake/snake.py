import pygame
import random
import button

# Initialise the game
pygame.init()

# Set the window dimensions
# Create window
width, height = 680, 480
background_colour = (255, 255, 255)
pygame.display.set_caption('MariaaAT/snake')
screen = pygame.display.set_mode((width, height))  # This actually created the window

field_size = 20, 14

# Create blocks and snake
block_w = width // field_size[0]
block_h = height // field_size[1]
snake = [(3, 3), (3, 2), (3, 1)]
colour_head = (43, 132, 0)
colour = (0, 255, 117)

# load button images
start_img = pygame.image.load("images/play_btn.png").convert_alpha()
exit_img = pygame.image.load("images/exit_btn.png").convert_alpha()

# Create a clock object to slow down the amount of frame rates per second
clock = pygame.time.Clock()

# Set the direction
dir = (0, 1)

# Set a move event
MOVE_EVENT = pygame.USEREVENT + 1
# pygame.event.post(pygame.event.Event(MOVE_EVENT)) # post makes the event happen inmediately
pygame.time.set_timer(pygame.event.Event(MOVE_EVENT), 1)  # The number says how much time passes until the event happens

# Set the treat
treat = (random.randint(0, field_size[0] - 1), random.randint(0, field_size[1] - 1))

# Dead variable
dead = False

font_go = pygame.font.SysFont('cochin', 32)
font_score = pygame.font.SysFont('cochin', 16)


def reset():
    global dead, snake, treat, score, dir
    dead = False
    snake = [(3, 3), (3, 2), (3, 1)]
    dir = (0, 1)
    treat = (random.randint(0, field_size[0] - 1), random.randint(0, field_size[1] - 1))
    score = 0


# Create function to write a message
def write_message(font, message, x, y):
    text = font.render(message, True, (0, 0, 0))
    screen.blit(text, (x, y))


score = 0

running = True
while running:
    for event in pygame.event.get():  # This pulls event from the event database, afterwards there's no more events in there
        if event.type == pygame.QUIT:
            running = False

        # Move the snake
        if event.type == MOVE_EVENT and not dead:
            snake = [((snake[0][0] + dir[0]) % field_size[0], (snake[0][1] + dir[1]) % field_size[1])] + snake[:-1]

            # Append treat to the snake
            # Check if the treat appears for the first time in the snake
            end_snake = snake[-1]
            if treat == snake[0]:
                snake.append(end_snake)
                score += 1
                while True:
                    treat = (random.randint(0, field_size[0] - 1), random.randint(0, field_size[1] - 1))
                    if treat not in snake:
                        break

            # Check collision
            if snake[0] in snake[1:]:
                dead = True

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

    # Score text written
    write_message(font_score, f"Score: {score}", 5, 10)

    # GAME OVER! message
    if dead:
        write_message(font_go, 'GAME OVER!', (width / 2) - 100, height / 2)
        # create button instances
        start_button = button.Button(90, 300, start_img, 0.6)
        exit_button = button.Button(390, 300, exit_img, 0.6)  # we work with pixels and not with the x, y coordinates
        if start_button.draw(screen): # You have to restart all the data
            reset()
        if exit_button.draw(screen):
            pygame.time.set_timer(pygame.event.Event(pygame.QUIT), 500)

    # Treat drawn
    pygame.draw.rect(screen, colour, pygame.Rect(treat[0] * block_w, treat[1] * block_h, block_w, block_h))

    # Snake drawn
    pygame.draw.rect(screen, colour_head, pygame.Rect(snake[0][0] * block_w, snake[0][1] * block_h, block_w, block_h))
    for block in snake[1:]:
        pygame.draw.rect(screen, colour,
                         pygame.Rect(block[0] * block_w, block[1] * block_h, block_w, block_h))

    pygame.display.flip()  # Update the window display

    clock.tick(60)

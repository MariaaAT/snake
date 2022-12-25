import pygame

width, height = 680, 480
background_colour = (255, 255, 255)
field_w = 20
field_h = 14

screen = pygame.display.set_mode((width, height))
screen.fill(background_colour)
pygame.display.flip()

snake = [(3, 3), (3, 2), (3, 1)]
colour_head = (43, 132, 0)
colour = (0, 255, 117)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

import pygame.mouse

class Button():
    # button instance created
    def __init__(self, x, y, image, scale):
        img_w = image.get_width()
        img_h = image.get_height()
        self.image = pygame.transform.scale(image, (int(img_w * scale), int(img_h * scale)))
        self.rect = self.image.get_rect()  # get a rectangle from it
        self.rect.topleft = (x, y)
        self.clicked = False

    # Draw the button on the screen
    def draw(self, surface):
        # allow different buttons do different things
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            # [] the number inside the bracket means the button we pressed on the mouse.
            # 0 is for left, 2 is for right
            # We equal that to 1 meaning that we pressed it
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, self.rect.x, self.rect.y)

        return action

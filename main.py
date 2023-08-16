import pygame

# define fps
clock = pygame.time.Clock()
FPS = 60

screen_width = 600
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")

# load image
bg = pygame.image.load("img/bg.png").convert_alpha()


def draw_bg():
    screen.blit(bg, (0, 0))


# game loop
run = True
while run:

    clock.tick(FPS)

    # draw background
    draw_bg()

    # event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update display
    pygame.display.update()

pygame.quit()

import pygame
from player


p = player.Player()
p.give_biscuit(player.tamagotchi.tamagotchis[0])
p.play_with(player.tamagotchi.tamagotchis[0])


print(player.tamagotchi.tamagotchis[0])


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(30)  # limits FPS

pygame.quit()

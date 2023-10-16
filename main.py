import pygame
import time
import random

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

BG = pygame.transform.scale(pygame.image.load("cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIyLTA1L3B4MTM2NjcxMC1pbWFnZS1rd3Z4eGVxcC5qcGc.webp"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_WIDTH = 60

def draw():
    WIN.blit(BG, (0, 0))
    pygame.display.update()

def main():
    run = True

    player = pygame.Rect()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw()

    pygame.quit()

if __name__ == "__main__":
    main()
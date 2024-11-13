
import pygame
import random



def main():
    try:
        pygame.init()

        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        mole_rect = mole_image.get_rect(topleft = (0,0))



        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if mole_rect.collidepoint(x, y):
                        x = random.randrange(0, 640//32)*32
                        y = random.randrange(0, 512//32)*32
                        mole_rect.topleft = (x,y)

            screen.fill("light green")

            # The window should be divided into a 20x16 grid of 32x32 squares

            # horizontal:
            for i in range(0, 512, 32):
                pygame.draw.line(screen, "black", (0, i), (640, i))

                # vertical:
                for j in range(0, 640, 32):
                    pygame.draw.line(screen, "black", (j, 0), (j, 512))

            # You can draw the mole with this snippet:
            # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
            screen.blit(mole_image, mole_rect)


            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

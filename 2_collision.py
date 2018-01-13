import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Badmeester')

clock = pygame.time.Clock()

block_size = 20
FPS = 30

font = pygame.font.SysFont(None, 25)


def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width / 2, display_height / 2])


def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 0
    lead_y_change = 0

    randPersonX = round (random.randrange(0, display_width-block_size))#/10.0)*10.0
    randPersonY = round (random.randrange(0, display_height-block_size))#/10.0)*10.0

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)

        PersonThickness = 30
        pygame.draw.rect(gameDisplay, red, [randPersonX, randPersonY, PersonThickness, PersonThickness])
        pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, block_size, block_size])
        pygame.display.update()

#        if lead_x >= randPersonX and lead_x <= randPersonX + PersonThickness:
#         if lead_y >= randPersonY and lead_y <= randPersonY + PersonThickness:
#            randPersonX = round(random.randrange(0, display_width - block_size))#/10.0) * 10.0
#            randPersonY = round(random.randrange(0, display_height - block_size))#/10.0) * 10.0

        if lead_x > randPersonX and lead_x < randPersonX + PersonThickness or lead_x + block_size > randPersonX and lead_x + block_size < randPersonX + PersonThickness:
         if lead_y > randPersonY and lead_y < randPersonY + PersonThickness or lead_y + block_size > randPersonY and lead_y + block_size < randPersonY + PersonThickness:
            randPersonX = round(random.randrange(0, display_width - block_size))#/10.0) * 10.0
            randPersonY = round(random.randrange(0, display_height - block_size))#/10.0) * 10.0


         elif lead_y + block_size > randPersonY and lead_y + block_size < randPersonY + PersonThickness:
            randPersonX = round(random.randrange(0, display_width - block_size))#/10.0) * 10.0
            randPersonY = round(random.randrange(0, display_height - block_size))#/10.0) * 10.0

        clock.tick(FPS)

    pygame.quit()
    quit()


gameLoop()
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

img = pygame.image.load('lifeguard.png')

clock = pygame.time.Clock()

block_size = 20
FPS = 15
score = 0

direction = "right"

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

def display_score(score):
    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text, [0,0])


def badmeester(block_size, badmeesterList):
    if direction == "right":
        head = pygame.transform.rotate(img, 270)

    if direction == "left":
        head = pygame.transform.rotate(img, 90)

    if direction == "up":
        head = img

    if direction == "down":
        head = pygame.transform.rotate(img, 180)

    gameDisplay.blit(head, (badmeesterList[-1][0], badmeesterList[-1][1]))

    for XnY in badmeesterList[:-1]:
        pygame.draw.rect(gameDisplay,
                         white,
                         [XnY[0],
                          XnY[1],
                          block_size,
                          block_size])

def text_objects(text, color, size):
    if size == "small":
        textSurface= smallfont.render(text, True, color)
    elif size == "medium":
        textSurface= medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2), (display_height / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)


def gameLoop():
    global direction
    score = 0
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 10
    lead_y_change = 0

    randPersonX = round (random.randrange(0,
                                          display_width-block_size))#/10.0)*10.0
    randPersonY = round (random.randrange(0,
                                          display_height-block_size))#/10.0)*10.0

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over",
                              red,
                              y_displace=-50,
                              size="large")
            message_to_screen("Press C to play again or Q to quit",
                              black,
                              50,
                              size="medium")
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
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)

        PersonThickness = 30
        pygame.draw.rect(gameDisplay,
                         red,
                         [randPersonX,
                          randPersonY,
                          PersonThickness,
                          PersonThickness])
        pygame.draw.rect(gameDisplay,
                         white,
                         [lead_x,
                          lead_y,
                          block_size,
                          block_size])

        badmeesterList = []
        badmeesterhead = []
        badmeesterhead.append(lead_x)
        badmeesterhead.append(lead_y)
        badmeesterList.append(badmeesterhead)
        badmeester(block_size, badmeesterList)
        display_score(score)

        pygame.display.update()

#        if lead_x >= randPersonX and lead_x <= randPersonX + PersonThickness:
#         if lead_y >= randPersonY and lead_y <= randPersonY + PersonThickness:
#            randPersonX = round(random.randrange(0, display_width - block_size))#/10.0) * 10.0
#            randPersonY = round(random.randrange(0, display_height - block_size))#/10.0) * 10.0

        if lead_x > randPersonX and lead_x < randPersonX + PersonThickness or lead_x + block_size > randPersonX and lead_x + block_size < randPersonX + PersonThickness:
         if lead_y > randPersonY and lead_y < randPersonY + PersonThickness or lead_y + block_size > randPersonY and lead_y + block_size < randPersonY + PersonThickness:
            randPersonX = round(random.randrange(0,
                                                 display_width - block_size))#/10.0) * 10.0
            randPersonY = round(random.randrange(0,
                                                 display_height - block_size))#/10.0) * 10.0
            score = score + 1


         elif lead_y + block_size > randPersonY and lead_y + block_size < randPersonY + PersonThickness:
            randPersonX = round(random.randrange(0,
                                                 display_width - block_size))#/10.0) * 10.0
            randPersonY = round(random.randrange(0,
                                                 display_height - block_size))#/10.0) * 10.0


        clock.tick(FPS)

    pygame.quit()
    quit()


gameLoop()


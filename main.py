import pygame
from database import DataBase
from gameWindow import gameScreen
from statsWindow import statsScreen
from methods import message_to_screen,text_to_button
pygame.font.init()
pygame.init()

gameIcon = pygame.image.load('sudokuicon.png')
pygame.display.set_icon(gameIcon)

db = DataBase("stats.txt")
win = pygame.display.set_mode((540,600))
pygame.display.set_caption('Sudoku v1.0')
black = (0,0,0)
white = (240,235,235)
red = (240,5,5)
yellow = (185,195,2)
green = (35,180,70)
light_green = (10,245,5)
blue = (5,10,235)



def gameIntro():
    intro = True
    while intro:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                intro =False
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] in range(230,331) and pygame.mouse.get_pos()[1] in range(300,341):
                pygame.draw.rect(win,light_green,(230,300,100,40))
                text_to_button("PLAY",black,230,300,100,40,win)
                pygame.display.update()

                gameScreen(win,db)
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] in range(230,331) and pygame.mouse.get_pos()[1] in range(360,401):
                pygame.draw.rect(win,yellow,(230,360,100,40))
                pygame.display.update()
                statsScreen(win,db)

        win.fill(white)
        message_to_screen("Sudoku", black, 80, 180, 200, win) #text,color,fontsize,x,y,win

        #playimg = pygame.image.load('play.png')
        #playimg = pygame.transform.scale(playimg, (80,80))
        #win.blit(playimg, (190,300))
        pygame.draw.rect(win,green,(230,300,100,40))
        text_to_button("PLAY",black,230,300,100,40,win)

        #statsimg = pygame.image.load('stats.png')
        #statsimg = pygame.transform.scale(statsimg, (87,87))
        #win.blit(statsimg, (290,299))
        pygame.draw.rect(win,yellow,(230,360,100,40))
        text_to_button("STATS",black,230,360,100,40,win)

        pygame.display.update()



gameIntro()

pygame.quit()
quit()

import pygame
#import mapeditor as ed

pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
screen=pygame.display.set_mode((640,480))

def menu():

   click=False
   while True:
        screen.fill((255,255,255))
        mx,my = pygame.mouse.get_pos()
        #here, i could not get the time to give the boxes some graphics,so the menu looks really unfinished
        button_1=pygame.Rect(220,200,200,50)
        button_2=pygame.Rect(220,300,200,50)
        button_3=pygame.Rect(220,400,200,50)

        if(button_1.collidepoint(mx,my)):
            if click:
                return 1
        if(button_2.collidepoint(mx,my)):
            if click:
                return 2
        if(button_3.collidepoint(mx,my)):
            if click:
                return 0
        pygame.draw.rect(screen,(0,0,0),button_1)
        pygame.draw.rect(screen,(0,0,0),button_2)
        pygame.draw.rect(screen,(0,0,0),button_3)
        click=False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click=True

        pygame.display.update()

if __name__=="__main__":
    menu()

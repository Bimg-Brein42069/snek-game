import pygame
#import mapeditor as ed

pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
screen=pygame.display.set_mode((640,480))

def menu():

   click=False
   button=[]
   for i in range(0,6):
       button.append(' ')
   while True:
        screen.fill((255,255,255))
        mx,my = pygame.mouse.get_pos()
        for i in range(0,6):
            button[i]=pygame.Rect(180 + 80*(i%3), 200 + 80*int(i/3), 50, 50)
            if button[i].collidepoint(mx,my):
                if click:
                    return i+1
            pygame.draw.rect(screen,(0,0,0),button[i])
        back_button=pygame.Rect(0,20,150,50)
        if back_button.collidepoint(mx,my):
            if click:
                return 0
        pygame.draw.rect(screen,(0,0,0),back_button)
        custom_button=pygame.Rect(500,400,150,50)
        if custom_button.collidepoint(mx,my):
            if click:
                return 7
        pygame.draw.rect(screen,(0,0,0),custom_button)

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

import pygame

pygame.init()
screen=pygame.display.set_mode((640,480))
font=pygame.font.Font(None,32)
color=(0,0,0)

def customsel():
    lvlq=font.render("level name?",True,color)
    name=''
    while True:
        screen.fill((255,255,255))
        screen.blit(levelq,(200,200))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
            elif event.type= pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return name
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode
        nameq=font.render(name,True,color)
        screen.blit(nameq,(200,240))
        pygame.display.update()


customsel()

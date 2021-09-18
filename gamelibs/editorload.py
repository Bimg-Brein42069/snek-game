import pygame

pygame.init()
screen=pygame.display.set_mode((640,480))
font=pygame.font.Font(None,32)
color=(0,0,0)

def lvlload(mapname):
    try:
        fileptr=open("custom/" + mapname,"r")
        return mapname
    except:
        return "File not found"

def lvlquery():
    nameq=font.render("file name?",True,color)
    name=''
    exception=font.render('',True,color)
    while True:
        screen.fill((155,188,15))
        screen.blit(nameq,(200,200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    namex=lvlload(name)
                    if namex == "File not found":
                        exception=font.render(namex,True,color)
                        name=''
                    else:
                        return namex
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_ESCAPE:
                    return 0
                else:
                    name += event.unicode
        namea=font.render(name,True,color)
        screen.blit(exception,(200,160))
        screen.blit(namea,(200,240))
        pygame.display.update()

def editorui():
    button_1=pygame.Rect(0,0,150,50)
    button_2=pygame.Rect(200,100,150,50)
    button_3=pygame.Rect(200,200,150,50)
    click=False
    while True:
        screen.fill((155,188,15))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        mx,my = pygame.mouse.get_pos()
        mclick = pygame.mouse.get_pressed()

        if mclick[0]:
            click=True

        if button_1.collidepoint(mx,my):
            if click:
                return 0
        if button_2.collidepoint(mx,my):
            if click:
                return 1
        if button_3.collidepoint(mx,my):
            if click:
                return 2

        pygame.draw.rect(screen,(0,0,0),button_1)
        pygame.draw.rect(screen,(0,0,0),button_2)
        pygame.draw.rect(screen,(0,0,0),button_3)

        click=False
        pygame.display.update()

if __name__ == '__main__':
    editorui()

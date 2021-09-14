import pygame
#import menu as m

#This thing exists because it would help me create levels easily, and to get your creativity up

pygame.init()
pygame.mixer.pre_init(44100,-16,2,512)
color=(15,56,15)
font=pygame.font.Font(None,32) 
screen=pygame.display.set_mode((640,480))

def save(mapattr):
    #this variable stays true until you enter a name
    inputed=True
    nameq=font.render("file name?",True,color)
    name='' 
    while inputed:
        screen.fill((155,188,15))
        screen.blit(nameq,(200,200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    inputed=False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode
        namea=font.render(name,True,color)
        screen.blit(namea,(200,240))
        pygame.display.update()
    #just for its exhibition, the level is saved in the custom directory, a feature could be coded to use those custom levels for gameplay
    addr="custom/"
    #addr="levels/"
    addr+=name
    name=addr
    #it gets the position of start of extension
    extpos=len(name)-4
    ext=name[extpos:]
    #check if the extension is .map,if not it appends to the map
    if ext != ".map":
        name+=".map"
    #write the map in the file
    with open(name,"w") as file:
        for xposarr in mapattr:
            for xpos in xposarr:
                file.write(str(xpos) + " ")
            file.write("\n")

#the editor function
def editor():
    #build the empty map
    mapattr=[]
    k=0
    while k<20:
        mapattrx=[]
        l=0
        while l<15:
            mapattrx.append(0)
            l+=1
        mapattr.append(mapattrx)
        k+=1

    wall=pygame.image.load("images/wall.png")
    
    editor_working=True
    while editor_working:
        screen.fill((155,188,15))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()

        mposx,mposy=pygame.mouse.get_pos()
        key=pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]: 
            dialog=True
            saveq=font.render("wanna save(y/n/c)", True, color)
            while dialog:
                screen.fill((155,188,15))
                screen.blit(saveq,(200,200))
                for event in pygame.event.get():
                    if event.type==pygame.KEYDOWN:
                        if event.key == pygame.K_y:
                            save(mapattr)
                            return 
                        elif event.key == pygame.K_n:
                            return 
                        elif event.key == pygame.K_c:
                            dialog=False
                    elif event.type==pygame.QUIT:
                        pygame.quit()
                        exit()
                pygame.display.update()


        mousebutton=pygame.mouse.get_pressed()
        #left click places a wall,right click removes it
        if mousebutton[0]:
            mapattr[int(mposx/32)][int(mposy/32)]=3
        elif mousebutton[2]:
            mapattr[int(mposx/32)][int(mposy/32)]=0

        i=0
        while i<20:
            j=0
            while j<15:
                if mapattr[i][j]==3:
                    screen.blit(wall,(i*32,j*32))
                j+=1
            i+=1
        pygame.display.update()

if __name__=="__main__":
    editor()



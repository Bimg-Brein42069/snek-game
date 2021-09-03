import pygame
import math
import random
import gamelibs.menu as m
import gamelibs.mapeditor as edit

pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()

def transpose(A):
    B=[]
    for i in range(len(A[0])):
        Bx=[]
        for j in range(len(A)):
            Bx.append(A[j][i])
        B.append(Bx)
    return B

def main():
    snake_body=pygame.image.load('images/snakebody.png')
    #  1
    #2 0 3
    snake_segs=[] 
    snake_segs.append(pygame.image.load('images/snaketail.png'))

    tileattr=[]
    with open("map0.txt","r") as file:
        data = file.readlines()
        tileattrx=[]
        for line in data:
            attr=line.split()
            j=0
            for i in attr:
                attr.pop(j)
                attr.insert(j,int(i))
                j+=1
            tileattrx.append(attr)
        tileattr.append(tileattrx)
    tileattr=tileattr[0]
    tileattr=transpose(tileattr)
    for i in range(0,3):
        snake_segs.append(snake_body)
    snake_dir=3
    snake_seg_size=32
    snake_posdir_array=[]
    for i in range(0,4):
        snake_posdir_array.append([(160-(snake_seg_size*(4-i)),160),snake_dir])
    time=0
    xvalprev=-500
    yvalprev=-500
    apple=pygame.image.load('images/apple.png')
    wall=pygame.image.load('images/wall.png')
    apple_eaten=True
    score=-1
    while True:
        time=(time+1)%6
        if apple_eaten:
            score+=1
            apple_pos=(snake_seg_size*random.randint(0,19),snake_seg_size*random.randint(0,14))
            apple_attr=tileattr[int(apple_pos[0]/32)][int(apple_pos[1]/32)]
            while apple_attr:
                apple_pos=(snake_seg_size*random.randint(0,19),snake_seg_size*random.randint(0,14))
                apple_attr=tileattr[int(apple_pos[0]/32)][int(apple_pos[1]/32)]
            tileattr[int(apple_pos[0]/32)][int(apple_pos[1]/32)]=1
            if score != 0:
                if snake_posdir_array[0][1] == 0:
                    snake_posdir_array.insert(0,[(snake_posdir_array[0][0][0],snake_posdir_array[0][0][1] -(snake_seg_size)),snake_posdir_array[0][1]])
                elif snake_posdir_array[0][1] == 1:
                    snake_posdir_array.insert(0,[(snake_posdir_array[0][0][0],snake_posdir_array[0][0][1] +(snake_seg_size)),snake_posdir_array[0][1]])
                elif snake_posdir_array[0][1] == 2:
                    snake_posdir_array.insert(0,[(snake_posdir_array[0][0][0]+snake_seg_size,snake_posdir_array[0][0][1]),snake_posdir_array[0][1]])
                elif snake_posdir_array[0][1] == 3:
                    snake_posdir_array.insert(0,[(snake_posdir_array[0][0][0]-snake_seg_size,snake_posdir_array[0][0][1]),snake_posdir_array[0][1]])
                snake_segs.append(snake_body)
            apple_eaten=False

        screen.fill((155,188,15))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
        keys=pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            exit()

        velX=0
        velY=0

        if time == 3:
            if keys[pygame.K_UP] and snake_dir!=0:
                snake_dir=1
            elif keys[pygame.K_DOWN] and snake_dir!=1:
                snake_dir=0
            elif keys[pygame.K_LEFT] and snake_dir!=3:
                snake_dir=2
            elif keys[pygame.K_RIGHT] and snake_dir!=2:
                snake_dir=3
        
            if snake_dir == 0:
                velY=-snake_seg_size
            elif snake_dir == 1:
                velY=snake_seg_size
            elif snake_dir == 2:
                velX=-snake_seg_size
            elif snake_dir == 3:
                velX=snake_seg_size            
       
        xval=snake_posdir_array[3+score][0][0] + velX
        yval=snake_posdir_array[3+score][0][1] - velY  
        headtile=tileattr[int(snake_posdir_array[3+score][0][0]/32)][int(snake_posdir_array[3+score][0][1]/32)]
        if snake_posdir_array[3+score][0]==apple_pos:
            apple_eaten=True
            tileattr[int(apple_pos[0]/32)][int(apple_pos[1]/32)]=0
        elif (headtile==2 or headtile==3) and time==4:
                return

        if xval > 640-snake_seg_size:
            xval=0
        if xval < 0:
            xval=640-snake_seg_size
        if yval > 480-snake_seg_size:
            yval=0
        if yval < 0:
            yval=480-snake_seg_size

        if (xval,yval) != (xvalprev,yvalprev):
            snake_posdir_array.append([(xval,yval),snake_dir])
            tileattr[int(snake_posdir_array[0][0][0]/32)][int(snake_posdir_array[0][0][1]/32)]=0
            snake_posdir_array.pop(0)




        for i in range(0,4+score):
            screen.blit(snake_segs[i],snake_posdir_array[i][0])
            if i!=3+score:   
                tileattr[int(snake_posdir_array[i][0][0]/32)][int(snake_posdir_array[i][0][1]/32)]=2
        k=0
        while k<20:
            l=0
            while l<15:
                if tileattr[k][l] == 3:
                    screen.blit(wall,(k*32,l*32))
                l+=1
            k+=1
        screen.blit(apple,apple_pos)
        xvalprev=xval
        yvalprev=yval
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    arg=m.menu()
    while arg:
        if arg == 1:
            main()
        elif arg == 2:
            edit.editor()
        arg=m.menu()





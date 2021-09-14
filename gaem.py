import pygame
import math
import random
import gamelibs.menu as m
import gamelibs.mapeditor as edit

#This game is incomplete as of now

pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()

def main():
    snake_body=pygame.image.load('images/snakebody.png')
    #The array to store each segment of the snake
    snake_segs=[] 
    snake_segs.append(pygame.image.load('images/snaketail.png'))
   
    tileattr=[]
    with open("level1.map","r") as file:
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
    #For some weird reason,it comes out as a [map] instead of map,so the following line mitigates this problem
    tileattr=tileattr[0]
    #snake starts with 3 body pieces and a tail piece
    for i in range(0,3):
        snake_segs.append(snake_body)
    snake_dir=3
    snake_seg_size=32
    #this contains the position and direction of movement of each segment of the snake, will be useful for animating it later
    snake_posdir_array=[]
    for i in range(0,4):
        snake_posdir_array.append([(160-(snake_seg_size*(4-i)),160),snake_dir])
    #time count
    time=0
    #previous values of x and y used in line 126 to prevent appending of snakesegments in segment list during the non-mobile frames
    xvalprev=-500
    yvalprev=-500
    apple=pygame.image.load('images/apple.png')
    wall=pygame.image.load('images/wall.png')
    #this variable is set true just so that the code in the check of apple_eaten gets to place the apple(this prevents rewriting of code for the check of the first apple)
    apple_eaten=True
    #score is set to -1, this proble is mitigated and score incremented to 0 in the check of apple_eaten
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
            #if the score is not zero(the snake has eaten at least 1 apple) then this code places the tail the correct way 
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
        
        #the snake will move in the correct time key(here it is 3, it can also be variable)
        if time == 3:
            #the control of the game works in this way
            #  1
            #2 0 3
            #the snake cannot snap its neck 180(think from the games perspective and it will eat itself up if those checks are not placed)
            if keys[pygame.K_UP] and snake_dir!=0:
                snake_dir=1
            elif keys[pygame.K_DOWN] and snake_dir!=1:
                snake_dir=0
            elif keys[pygame.K_LEFT] and snake_dir!=3:
                snake_dir=2
            elif keys[pygame.K_RIGHT] and snake_dir!=2:
                snake_dir=3
            #assign the direction of its movement by changing the velocities
            if snake_dir == 0:
                velY=-snake_seg_size
            elif snake_dir == 1:
                velY=snake_seg_size
            elif snake_dir == 2:
                velX=-snake_seg_size
            elif snake_dir == 3:
                velX=snake_seg_size            
       #move the snake
        xval=snake_posdir_array[3+score][0][0] + velX
        yval=snake_posdir_array[3+score][0][1] - velY  
        #here the head tile attribute is set in advance
        headtile=tileattr[int(snake_posdir_array[3+score][0][0]/32)][int(snake_posdir_array[3+score][0][1]/32)]
        #if snake's head meets the apple, the apple is deemed to be eaten
        #(ofc u could add some frames for his mouth opening,but animation takes time :[ )
        if snake_posdir_array[3+score][0]==apple_pos:
            apple_eaten=True
            #the tail tile attribute is set to 0(there is nothing)
            tileattr[int(apple_pos[0]/32)][int(apple_pos[1]/32)]=0
        #if in the next frame the snake hits a wall he dies
        elif (headtile==2 or headtile==3) and time==4:
                return
        
        #if the snake moves out of the screen, he is brought back to it properly
        if xval > 640-snake_seg_size:
            xval=0
        if xval < 0:
            xval=640-snake_seg_size
        if yval > 480-snake_seg_size:
            yval=0
        if yval < 0:
            yval=480-snake_seg_size

        #the appends only happen when the snake moves
        if (xval,yval) != (xvalprev,yvalprev):
            snake_posdir_array.append([(xval,yval),snake_dir])
            tileattr[int(snake_posdir_array[0][0][0]/32)][int(snake_posdir_array[0][0][1]/32)]=0
            snake_posdir_array.pop(0)

        #draw the snake
        for i in range(0,4+score):
            screen.blit(snake_segs[i],snake_posdir_array[i][0])
            #this if statement mitigated a rare bug, where the game crashes due to a list overflow error
            if i!=3+score:   
                tileattr[int(snake_posdir_array[i][0][0]/32)][int(snake_posdir_array[i][0][1]/32)]=2
        #draw the walls
        k=0
        while k<20:
            l=0
            while l<15:
                if tileattr[k][l] == 3:
                    screen.blit(wall,(k*32,l*32))
                l+=1
            k+=1
        #draw the apple
        screen.blit(apple,apple_pos)
        #set the previous positions to be the new ones after movement
        xvalprev=xval
        yvalprev=yval
        #update the display
        pygame.display.update()
        #cap fps to 60(as in this case the time is counted by a fixed value)
        clock.tick(60)

if __name__ == "__main__":
    #load the menu
    arg=m.menu()
    while arg:
        #set the buttons,if arg==0 the program exits
        if arg == 1:
            main()
        elif arg == 2:
            edit.editor()
        arg=m.menu()





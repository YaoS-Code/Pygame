import pygame
import os
import time
os.system("clear")
pygame.init()
X = 1000
Y = 600
sprite = ["1.png","2.png","3.png","4.png","5.png","6.png","7.png","8.png","9.png","10.png"]
scrn = pygame.display.set_mode((X, Y))
path = os.path.join(os.path.dirname(__file__), './sprite/', sprite[0])
path_background = os.path.join(os.path.dirname(__file__), './background/', 'brick.jpeg')
img_background = pygame.image.load(path_background)
img = pygame.image.load(path)
img_flip = pygame.transform.flip(img, True, False)
xPos = X/2-img.get_width()/2
yPos = -img.get_height()/2
pygame.display.set_caption('2D Game')
pygame.display.flip()
status = True
speed = 0
acceleration = 0.5
fps = 60
clock = pygame.time.Clock()
xSpeed =0
xAcc = 0
count = 0
# in physics, left / down means negative. up and right means positive
while status:
    count += 1
    path = os.path.join(os.path.dirname(__file__), './sprite/', sprite[count//5%10])
    print(speed)
        
    img = pygame.image.load(path)
    img_flip = pygame.transform.flip(img, True, False)
    for event in pygame.event.get():
 
        if event.type == pygame.QUIT:
            status = False

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE] and yPos >= 400:
            print(yPos)
            speed = -10
            
        if keys_pressed[pygame.K_LEFT]:
            xSpeed = -2
        elif keys_pressed[pygame.K_RIGHT]:
            xSpeed = +2
        else: 
            xSpeed =0
                
    if xPos >= 880:
        xPos = 880
    if xPos <= 10:
        xPos = 10
    if yPos >= 400:
        yPos = 400
    if yPos <400:
        speed = speed + acceleration    
    xPos += xSpeed
    yPos += speed
    scrn.fill("white")
    scrn.blit(img_background,(0-img_background.get_width()/2,0-img_background.get_height()/2))
    if xSpeed >=0:
        scrn.blit(img,(xPos, yPos))
    else:
        scrn.blit(img_flip, (xPos, yPos))
        
    pygame.display.update()
    clock.tick(fps)
pygame.quit()

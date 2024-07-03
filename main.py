import pygame
pygame.init()

window = pygame.display.set_mode((1200, 400)) #Display the new window.
track = pygame.image.load('track6.png') #Road added into the window.
car = pygame.image.load('tesla.png') #Car added into the window.
car = pygame.transform.scale(car, (30, 60)) #Car resize.

#Car initial coordinate.
carX = 150
carY = 300

#Create a virtual camera and initial camera position.
camX_offset = 0
camY_offset = 0
focalDis = 25 #How much distance camera will see.

#Car's initial direction.
direction = 'up'

clock = pygame.time.Clock() #Added a clock.
drive = True

while drive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False
            
    clock.tick(60)
    #How much virtual camera will see ahead.
    camX = carX + camX_offset + 15
    camY = carY + camY_offset + 15
    
    #Color pixels on the front of the virtual camera.
    upperPixel = window.get_at((camX, camY - focalDis))[0]
    downPixel = window.get_at((camX, camY + focalDis))[0]
    rightPixel = window.get_at((camX + focalDis, camY))[0]
    #print(up_px, right_px, down_px)

    #Change direction (take turn)
    if direction == 'up' and upperPixel != 255 and rightPixel == 255:
        direction = 'right'
        camX_offset = 30 #Change camera position.
        car = pygame.transform.rotate(car, -90) #Car change his direction and rotated.
        
    elif direction == 'right' and rightPixel != 255 and downPixel == 255:
        direction = 'down'
        carX = carX + 30
        
        #Change camera position.
        camX_offset = 0
        camY_offset = 30
        car = pygame.transform.rotate(car, -90) #Car change his direction and rotated.
        
    elif direction == 'down' and downPixel != 255 and rightPixel == 255:
        direction = 'right'
        carY = carY + 30
        camX_offset = 30
        camY_offset = 0
        car = pygame.transform.rotate(car, 90)
        
    elif direction == 'right' and rightPixel != 255 and upperPixel == 255:
        direction = 'up'
        carX = carX + 30
        camX_offset = 0
        car = pygame.transform.rotate(car, 90) #Car change his direction and rotated.
        
    #Car speed change.
    if direction == 'up' and upperPixel == 255:
        carY = carY - 2
    elif direction == 'right' and rightPixel == 255:
        carX = carX + 2
    elif direction == 'down' and downPixel == 255:
        carY = carY + 2
    
    #Update the pygame window by using block image transfer(blit).  
    window.blit(track, (0, 0))
    window.blit(car, (carX, carY)) #Update the car position.
    pygame.draw.circle(window, (0, 255, 0), (camX, camY), 5, 5) #Size of the virtual camera.
    pygame.display.update()
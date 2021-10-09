import pygame

pygame.init()
width = 500
height = 500
screen = pygame.display.set_mode((width, height))
running = True

image = pygame.image.load("ball.png").convert()

xBall = width/2
yBall = height/2
vx = 5
vy = 0
dt = 1
G = 9.81
vitesse = [vx,vy]


clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        vx = - 5
    if pressed[pygame.K_RIGHT]:
        vx = + 5
    if pressed[pygame.K_UP]:
        vy = 20
        dt = 1
    if pressed[pygame.K_DOWN]:
        running = False

    #Gravité

    xBall = xBall + vx * dt
    yBall = yBall - vy * dt
    vx = vx
    vy = vy - 0.1 * G * dt

    #Collision bords
    if xBall < 0 :  #bord gauche
        vx = 0
        xBall = 0
    if xBall > width - image.get_width():   #bord droit
        vx = 0
        xBall = width - image.get_width()
    if yBall < 0 :  #bord haut
        vy = 0
        yBall = 0
    if yBall + image.get_height() > height :    #bord bas
        vy = 0
        yBall = height - image.get_height()




    #Gestion souris



    screen.fill((0, 0, 0))
    screen.blit(image, (xBall, yBall))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
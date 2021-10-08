import pygame

pygame.init()
width = 1000
height = 1000
screen = pygame.display.set_mode((width, height))
running = True

image = pygame.image.load("ball.png").convert()

xBall = width/2
yBall = height/2
gravite = 1

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        xBall -= 5
    if pressed[pygame.K_RIGHT]:
        xBall += 5
    if pressed[pygame.K_UP]:
        gravite = -30
    if pressed[pygame.K_DOWN]:
        yBall += 1

    #Collision bords
    if xBall < 0 :
        xBall += 5
    if xBall > width - image.get_width():
        xBall -= 5
    if yBall < 0 :
        yBall = 0
        gravite = 0
    if yBall > height - image.get_height() - gravite :
        yBall = height - image.get_height() - gravite


    #Gravité
    if gravite < 20 :
        gravite += 1
    yBall += gravite


    #Gestion souris



    screen.fill((0, 0, 0))
    screen.blit(image, (xBall, yBall))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()

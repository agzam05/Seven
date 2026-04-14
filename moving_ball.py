import pygame
import sys
pygame.init()
WIDTH, HEIGHT= 600, 600
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving_ball")
clock=pygame.time.Clock()
x, y= WIDTH//2, HEIGHT//2
radius=25
speed=20
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x-radius-speed>=0:
        x-=speed
    if keys[pygame.K_RIGHT] and x+radius+speed<=WIDTH:
        x+=speed
    if keys[pygame.K_UP] and y-radius-speed>=0:
        y-=speed
    if keys[pygame.K_DOWN]and y+radius+speed<=HEIGHT:
        y+=speed
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255,0 ,0), (x,y), radius)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()

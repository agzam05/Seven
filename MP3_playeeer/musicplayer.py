import pygame
pygame.init()
pygame.mixer.init()
WIDTH, HEIGHT=800, 600
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Musicplayer")
font=pygame.font.Font(None, 36)
clock=pygame.time.Clock()
playlist=["ol.mp3","aa.mp3" ]
current=0
def play_music():
    pygame.mixer.music.load(playlist[current])
    pygame.mixer.music.play()
running=True
while running:
    screen.fill((0,0,0))
    text=font.render(f"The current music is {playlist[current]}",True, (255,255,255))
    screen.blit(text, (20, 80))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_p:
                play_music()
            elif event.key==pygame.K_s:
                pygame.mixer.music.stop()
            elif event.key==pygame.K_n:
                current+=1
                if current>=len(playlist):
                    currrent=0
                play_music()
            elif event.key==pygame.K_b:
                current=-1
                if current<0:
                    current=len(playlist)
                play_music()
            elif event.key==pygame.K_q:
                pygame.quit()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
import pygame
pygame.mixer.init()

pygame.init()
screen = pygame.display.set_mode((800, 800))

songs = ["taspa.mp3","mahabbatym.mp3","men-dep-oila.mp3",]
current_music = 0
pygame.mixer.music.load(songs[current_music])
pygame.mixer.music.play()
background = pygame.image.load("main-clock.png")
background_rect = background.get_rect()
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play()
            elif event.key == pygame.K_RIGHT:
                current_music = (current_music + 1) % len(songs)
                pygame.mixer.music.load(songs[current_music])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_music = (current_music - 1) % len(songs)
                pygame.mixer.music.load(songs[current_music])
                pygame.mixer.music.play()

    screen.blit(background, (0, 0))
    pygame.display.flip()
pygame.quit() 
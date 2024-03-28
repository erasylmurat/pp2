import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ball")


x = 400
y = 300

clock = pygame.time.Clock()

while True:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if y+21<=screen_height:
                    y += 20

            if event.key == pygame.K_UP:
                if y-21>=0:
                    y -= 20
            if event.key == pygame.K_RIGHT:
                if x+21<=screen_width:
                    x += 20   
            if event.key == pygame.K_LEFT:
                if x-21>=0:
                    x -= 20

    screen.fill((0, 0, 0))
    player = pygame.draw.circle(screen, (0, 0, 255), (x, y), 25)
    pygame.display.update()
    clock.tick(60)


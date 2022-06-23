import sys
import pygame
import random
pygame.init()

size = width, height = 800, 600
speed_unit = 10
speed = [speed_unit, 0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()
head_pos = [400, 300]
snake_head = pygame.draw.rect(surface=screen, color="green", rect=[head_pos[0], head_pos[1], 15, 15])

body_pos = [
    [400, 300], [390, 300], [380, 300], [370, 300]
]
fruit_pos = [random.randrange(1, 80) * 10,
             random.randrange(1, 60) * 10]
fruit_spawn = True
score = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and speed[1] >= 0:
                speed = [0, speed_unit]
            if event.key == pygame.K_UP and speed[1] <= 0:
                speed = [0, -speed_unit]
            if event.key == pygame.K_LEFT and speed[0] <= 0:
                speed = [-speed_unit, 0]
            if event.key == pygame.K_RIGHT and speed[0] >= 0:
                speed = [speed_unit, 0]
    ballrect = ballrect.move(speed)

    if abs(head_pos[0]-fruit_pos[0]) < 5 and abs(head_pos[1]-fruit_pos[1]) < 5:
        print("food eaten score increased")
        body_pos.append(body_pos[len(body_pos)-1])
        fruit_spawn = False
        score += 1

    for pos in body_pos[1:]:
        if head_pos[0] == pos[0] and head_pos[1] == pos[1]:
            sys.exit()

    if not fruit_spawn:
        fruit_pos = [random.randrange(1, 80) * 10,
                     random.randrange(1, 60) * 10]
    fruit_spawn = True

    screen.fill(black)
    for i in range(len(body_pos)-1):
        body_pos[len(body_pos)-1-i] = body_pos[len(body_pos)-2-i]
        pos = body_pos[len(body_pos)-1-i]
        pygame.draw.rect(surface=screen, color="green", rect=[pos[0], pos[1], 10, 10])
    head_pos[0] += speed[0]
    head_pos[1] += speed[1]
    snake_head.move(speed)
    if head_pos[0] < 0 or head_pos[0] > width:
        sys.exit()
    if head_pos[1] < 0 or head_pos[1] > height:
        sys.exit()
    body_pos[0] = [head_pos[0], head_pos[1]]
    pygame.draw.rect(surface=screen, color="green", rect=[head_pos[0], head_pos[1], 10, 10])
    pygame.draw.rect(surface=screen, color="red", rect=[fruit_pos[0], fruit_pos[1], 10, 10])
    score_font = pygame.font.SysFont("Courier", 24)
    score_surface = score_font.render('Score : ' + str(score), True, "white")
    score_rect = score_surface.get_rect()
    screen.blit(score_surface, score_rect)
    pygame.display.flip()
    pygame.time.wait(round(100/(score+1)**(1./3.)))

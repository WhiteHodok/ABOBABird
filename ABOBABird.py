import pygame
import random
import time

pygame.init()

screen_width = 288
screen_height = 512
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ABOBA Bird")

bird_color = (255, 255, 0)
bird_size = (30, 30)
bird_x = 50
bird_y = 200
bird_rect = pygame.Rect(bird_x, bird_y, bird_size[0], bird_size[1])

pipe_color = (0, 255, 0)
pipe_width = 50
pipe_gap = 120
pipe_x = screen_width
pipe_height = random.randint(50, 350)
pipe_rect_top = pygame.Rect(pipe_x, 0, pipe_width, pipe_height)
pipe_rect_bottom = pygame.Rect(pipe_x, pipe_height + pipe_gap, pipe_width, screen_height - pipe_height - pipe_gap)

score = 0
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y -= 50
                time.sleep(0.2)  # задержка в 0.2 секунды , это тоже можно поменять для скорости

    bird_y += 1  # Это менять для скорости
    pipe_x -= 3  # И это

    if pipe_x < -pipe_width:
        pipe_x = screen_width
        pipe_height = random.randint(50, 350)
        pipe_rect_top = pygame.Rect(pipe_x, 0, pipe_width, pipe_height)
        pipe_rect_bottom = pygame.Rect(pipe_x, pipe_height + pipe_gap, pipe_width, screen_height - pipe_height - pipe_gap)

    bird_rect = pygame.Rect(bird_x, bird_y, bird_size[0], bird_size[1])

    if bird_y > screen_height - bird_size[1] or bird_y < 0:
        game_over = True

    if bird_rect.colliderect(pipe_rect_top) or bird_rect.colliderect(pipe_rect_bottom):
        game_over = True

    if pipe_x == bird_x:
        score += 1

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, bird_color, bird_rect)

    # Обновление координат труб
    pipe_rect_top.left = pipe_x
    pipe_rect_bottom.left = pipe_x
    pygame.draw.rect(screen, pipe_color, pipe_rect_top)
    pygame.draw.rect(screen, pipe_color, pipe_rect_bottom)

    font = pygame.font.SysFont(None, 30)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    if game_over:
        font = pygame.font.SysFont(None, 50)
        text = font.render("Game Over!", True, (255, 255, 255))
        screen.blit(text, (100, 200))

    pygame.display.update()

pygame.quit()









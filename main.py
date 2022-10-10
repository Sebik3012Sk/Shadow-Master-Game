import pygame
import random

pygame.init()

WIDTH = 1000
HEIGHT = 500

global color_speacial

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Shadow Game")

color_speacial = pygame.Color("#b14e06")

fps = 60
clock = pygame.time.Clock()

# load images
bg_image = pygame.image.load("img/bg-image.png")
player = pygame.image.load("img/player.png")
shadow_enemy = pygame.image.load("img/shodow-enemy.png")
bullet = pygame.image.load("img/bullet.png")
enemy_shot = pygame.image.load("img/enemy-shot.png")
icon = pygame.image.load("img/icon-game.png")


pygame.display.set_icon(icon)

# fonts 
score = 0
font_score = pygame.font.SysFont("Arial",48)
game_over = pygame.font.SysFont("Arial",48)


player_rect = player.get_rect()
shadow_enemy_rect = shadow_enemy.get_rect()
bullet_rect = bullet.get_rect()
enemy_shot_rect = enemy_shot.get_rect()

player_rect.centerx = 250
player_rect.centery = 385

enemy_shot_rect.centerx = 1060 - 28
enemy_shot_rect.centery = shadow_enemy_rect.centery + 140

shadow_enemy_rect.centerx = 1060
shadow_enemy_rect.centery = random.randint(85,HEIGHT - 85)

x = 0
y = 0

vel = 10

enemy_speed = 3

run = True

while run:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False

    keys = pygame.key.get_pressed()

    if(keys[pygame.K_LEFT] and player_rect.left > 0):
        player_rect.x -= vel
    elif(keys[pygame.K_RIGHT] and player_rect.right < WIDTH):
        player_rect.x += vel
    elif(keys[pygame.K_UP] and player_rect.top > 0):
        player_rect.y -= vel
    elif(keys[pygame.K_DOWN] and player_rect.bottom < HEIGHT):
        player_rect.y += vel

    if(keys[pygame.K_f]):
        bullet_rect.centerx = player_rect.x + 6
        bullet_rect.centery = player_rect.y + 43
        pygame.time.delay(10)
    
    if bullet_rect.centerx < 0:
        pass
    else:
        bullet_rect.centerx += vel
    
    text_game = ""

    if shadow_enemy_rect.centerx < 0:
        text_game = "Game Over"
        shadow_enemy_rect.centerx -= enemy_speed
    else:
        shadow_enemy_rect.centerx -= enemy_speed

    text_game_over = game_over.render(text_game,True,(255,255,255))

    if(bullet_rect.colliderect(shadow_enemy_rect)):
        score += 1
        shadow_enemy_rect.centerx = 1060
        shadow_enemy_rect.centery = random.randint(85,HEIGHT - 85)
        enemy_speed += 0.5

        if shadow_enemy_rect.centerx < 0:
            shadow_enemy_rect.centerx -= enemy_speed
        else:
            shadow_enemy_rect.centerx -= enemy_speed

    if(enemy_shot_rect.centerx < 0):
        enemy_shot_rect.centerx -= vel
    else:
        enemy_shot_rect.centerx -= 14

    font_game_over = pygame.font.SysFont("Kokila",48)
    text_game_end = ""

    if(enemy_shot_rect.colliderect(player_rect)):
        text_game_end = "Game Over"
    
    game_over_text = font_game_over.render(text_game_end,True,color_speacial)
    text_score = font_score.render(f"Kill : {score}",True,color_speacial)


    screen.blit(bg_image,(0,0))
    screen.blit(player,(player_rect.x,player_rect.y))
    screen.blit(shadow_enemy,shadow_enemy_rect)
    screen.blit(bullet,bullet_rect)
    screen.blit(shadow_enemy,shadow_enemy_rect)
    screen.blit(text_score,(35,35))
    screen.blit(text_game_over,(400,200))
    screen.blit(enemy_shot,enemy_shot_rect)
    screen.blit(game_over_text,(400,200))
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
import pygame
import random
from sys import exit

def increase_score():
    pass

pygame.init()
vaizdas = pygame.display.set_mode((800, 600))
vaizdas.fill('White')
pygame.display.set_caption('Lietus')
clock = pygame.time.Clock()

sriftas = pygame.font.Font('Fonts/orange_juice.ttf', 50)

dangaus_tekstura = pygame.image.load('graphics/rain-clouds.png').convert_alpha()
zoles_tekstura = pygame.image.load('graphics/grass.png').convert_alpha()
laso_tekstura = pygame.image.load('graphics/raindrop_res.png').convert_alpha()
laso_rect = laso_tekstura.get_rect(midbottom=(0, 0))

personazas = pygame.image.load('graphics/doll_200px.png').convert_alpha()
personazas_rect = personazas.get_rect(midbottom=(400, 600))

sriftas_tekstura = sriftas.render('Taškai: ', False, 'White')

score = 0
zaidimas_veikia = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if zaidimas_veikia:
            if event.type == pygame.KEYDOWN and event.type == pygame.K_SPACE:
                    print('Paspaustas "Space"')

        else:
            if event.type == pygame.KEYDOWN and event.type == pygame.K_SPACE:
                zaidimas_veikia = True
                laso_rect.y = 0



    if zaidimas_veikia:
        vaizdas.blit(dangaus_tekstura, (0, 0))
        vaizdas.blit(zoles_tekstura, (0, 459))
        laso_rect.y += 6


        if laso_rect.bottom > 600:
            laso_rect.bottom = 0
            laso_rect.x = random.randint(0, 800)
            score += 1

        score_max = 5
        if score_max < score:
            laso_rect.y += 4
            score_max += 5




        sriftas_taskai = sriftas.render(f'{score}', False, 'White')
        vaizdas.blit(sriftas_taskai, (200, 10))
        vaizdas.blit(laso_tekstura, laso_rect)
        vaizdas.blit(sriftas_tekstura, (10, 10))
        vaizdas.blit(personazas, personazas_rect)

        paspaudimai = pygame.key.get_pressed()
        if paspaudimai[pygame.K_LEFT]:
            personazas_rect.left -= 5
        if paspaudimai[pygame.K_RIGHT]:
            personazas_rect.left += 5


        if laso_rect.colliderect(personazas_rect):
            zaidimas_veikia = False

    else:
        vaizdas.fill('Black')
        pabaigos_pranesimas = sriftas.render('Pralaimėjai', False, 'White')
        vaizdas.blit(pabaigos_pranesimas, (300,50))



    pygame.display.update()
    clock.tick(60)

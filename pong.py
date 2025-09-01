import pygame
import sys
from objetos import Raquete, Bola

pygame.init()

# Configurações da tela
LARGURA = 800
ALTURA = 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pong com Objetos")

# Cria objetos
raquete_esq = Raquete(20, ALTURA//2 - 50, 20, 100, 5)
raquete_dir = Raquete(LARGURA - 40, ALTURA//2 - 50, 20, 100, 5)
bola = Bola(LARGURA//2, ALTURA//2, 15, 4, 4)

placar_esq = 0
placar_dir = 0

# Fonte para exibir o placar
fonte = pygame.font.SysFont(None, 50)


# Loop principal
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    raquete_esq.mover(pygame.K_w, pygame.K_s, teclas, ALTURA)
    raquete_dir.mover(pygame.K_UP, pygame.K_DOWN, teclas, ALTURA)
    bola.mover(ALTURA)
    # Checa colisão com raquete esquerda
    if bola.get_rect().colliderect(raquete_esq.get_rect()):
        bola.vel_x *= -1

    # Checa colisão com raquete direita
    if bola.get_rect().colliderect(raquete_dir.get_rect()):
        bola.vel_x *= -1
    
    # Bola passou da raquete esquerda
    if bola.x < 0:
        placar_dir += 1
        bola.x = LARGURA // 2
        bola.y = ALTURA // 2
        bola.vel_x *= -1  # muda direção da bola

    # Bola passou da raquete direita
    if bola.x > LARGURA:
        placar_esq += 1
        bola.x = LARGURA // 2
        bola.y = ALTURA // 2
        bola.vel_x *= -1



    TELA.fill((0,0,0))
    # Renderiza o placar
    texto_placar = fonte.render(f"{placar_esq}  |  {placar_dir}", True, (255,255,255))
    TELA.blit(texto_placar, (LARGURA//2 - texto_placar.get_width()//2, 20))

    raquete_esq.desenhar(TELA)
    raquete_dir.desenhar(TELA)
    bola.desenhar(TELA)
    pygame.display.flip()

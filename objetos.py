import pygame

# Classe Raquete
class Raquete:
    def __init__(self, x, y, largura, altura, vel):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.vel = vel

    def desenhar(self, tela):
        pygame.draw.rect(tela, (255, 255, 255), (self.x, self.y, self.largura, self.altura))

    def mover(self, tecla_cima, tecla_baixo, teclas_pressionadas, altura_tela):
        if teclas_pressionadas[tecla_cima] and self.y > 0:
            self.y -= self.vel
        if teclas_pressionadas[tecla_baixo] and self.y + self.altura < altura_tela:
            self.y += self.vel
    
    # NOVO MÉTODO PARA COLISÃO
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)


# Classe Bola
class Bola:
    def __init__(self, x, y, raio, vel_x, vel_y):
        self.x = x
        self.y = y
        self.raio = raio
        self.vel_x = vel_x
        self.vel_y = vel_y

    def desenhar(self, tela):
        pygame.draw.circle(tela, (255, 255, 255), (self.x, self.y), self.raio)

    def mover(self, altura_tela):
        self.x += self.vel_x
        self.y += self.vel_y

        # Rebote nas paredes superior e inferior
        if self.y - self.raio <= 0 or self.y + self.raio >= altura_tela:
            self.vel_y *= -1

    # NOVO MÉTODO PARA COLISÃO
    def get_rect(self):
        return pygame.Rect(self.x - self.raio, self.y - self.raio, self.raio*2, self.raio*2)


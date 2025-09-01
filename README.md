# Pong em Pygame

## Descrição
Este é um projeto simples do clássico jogo **Pong**, desenvolvido em Python usando a biblioteca **Pygame**.  
O objetivo é criar um jogo 2D funcional, com bola, raquetes e placar.  
É ideal para iniciantes aprenderem lógica de programação, manipulação de eventos e gráficos 2D.

---

## Pré-requisitos
- Python 3.x
- Pygame 2.x

---

## Instalação

1. Clone ou baixe o projeto.
2. Crie e ative um ambiente virtual (recomendado):

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

## Instale as dependências:

```bash
pip install -r requirements.txt


# Principais funções e métodos do Pygame usados
Inicialização e encerramento
pygame.init()         # Inicializa o Pygame
pygame.quit()         # Encerra o Pygame
clock = pygame.time.Clock()  # Objeto para controlar FPS

Tela e janelas
pygame.display.set_mode((largura, altura))  # Cria a janela
pygame.display.set_caption("Título")       # Define o título
pygame.display.flip()                       # Atualiza toda a tela
pygame.display.update()                     # Atualiza parte específica da tela

Eventos e entrada
pygame.event.get()        # Retorna lista de eventos
pygame.QUIT               # Evento de fechar a janela
pygame.KEYDOWN            # Evento de tecla pressionada
pygame.KEYUP              # Evento de tecla liberada
pygame.key.get_pressed()  # Retorna estado de todas as teclas

Desenho e gráficos
tela.fill(cor)                                      # Preenche a tela com uma cor
pygame.draw.rect(tela, cor, (x, y, largura, altura))   # Desenha retângulo
pygame.draw.circle(tela, cor, (x, y), raio)           # Desenha círculo
pygame.draw.line(tela, cor, (x1, y1), (x2, y2), largura) # Desenha linha

Imagens
pygame.image.load("arquivo.png")               # Carrega imagem
tela.blit(imagem, (x, y))                      # Desenha imagem na tela
pygame.transform.scale(imagem, (largura, altura))  # Redimensiona imagem
pygame.transform.rotate(imagem, graus)            # Rotaciona imagem

Sons e música
pygame.mixer.init()                   # Inicializa áudio
pygame.mixer.Sound("som.wav")         # Carrega efeito sonoro
som.play()                             # Toca efeito sonoro
pygame.mixer.music.load("musica.mp3") # Carrega música de fundo
pygame.mixer.music.play(-1)           # Toca música em loop (-1 = infinito)
pygame.mixer.music.stop()             # Para a música

Tempo e FPS
clock = pygame.time.Clock()  # Objeto de controle de FPS
clock.tick(fps)              # Limita o jogo a 'fps' quadros por segundo
pygame.time.get_ticks()      # Retorna tempo desde o início em milissegundos

Colisões
rect.colliderect(outro_rect)  # Retorna True se houver colisão entre dois retângulos


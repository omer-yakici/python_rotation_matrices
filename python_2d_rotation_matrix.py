import pygame
import sys

width, height = 500, 500
bg_color = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("2D Dönme Matrisi Animasyonu")

clock = pygame.time.Clock()

# Başlangıç vektörü
v = pygame.math.Vector2(1, 0)
v_length = 100  # Uzunluk sabit olmalı
v.scale_to_length(v_length)  

# Döndürme açısı
theta = 0

# Ana oyun döngüsü
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Döndürme matrisini uygula
    rotated_vector = v.rotate(theta)

    screen.fill(bg_color)
  
    pygame.draw.line(screen, (0, 0, 255), (width / 2, height / 2), (width / 2 + v.x, height / 2 + v.y), 2)
  
    pygame.draw.line(screen, (255, 0, 0), (width / 2, height / 2), (width / 2 + rotated_vector.x, height / 2 + rotated_vector.y), 2)

    pygame.display.flip()

    clock.tick(60)

    theta =theta + 1

pygame.quit()
sys.exit()

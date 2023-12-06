import pygame
import sys
import numpy as np
from pygame.locals import *

pygame.init()

width, height = 1600, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("3D Dönme")

clock = pygame.time.Clock()

# Küpün köşe noktalarının tanımlanması
vertices = np.array([
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1]
])

# Bağlantı noktaları
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

# Dönme matrisini tanımla
def rotate_x(theta):
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    rotation_matrix = np.array([
        [1, 0, 0],
        [0, cos_theta, -sin_theta],
        [0, sin_theta, cos_theta]
    ])
    return rotation_matrix

def rotate_y(theta):
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    rotation_matrix = np.array([
        [cos_theta, 0, sin_theta],
        [0, 1, 0],
        [-sin_theta, 0, cos_theta]
    ])
    return rotation_matrix

def rotate_z(theta):
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    rotation_matrix = np.array([
        [cos_theta, -sin_theta, 0],
        [sin_theta, cos_theta, 0],
        [0, 0, 1]
    ])
    return rotation_matrix

#Ana döngüyü başlat.
theta_x = 0
theta_y = 0
theta_z = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    screen.fill((255, 255, 255))

    # Dönme matrislerini kullanarak küpü döndür
    rotation_matrix_x = rotate_x(theta_x)
    rotation_matrix_y = rotate_y(theta_y)
    rotation_matrix_z = rotate_z(theta_z)

    rotated_vertices = vertices.dot(rotation_matrix_x).dot(rotation_matrix_y).dot(rotation_matrix_z)

    # 2D ekran koordinatlarına dönüştür
    projected_vertices = (rotated_vertices + 5) * 100  # Küpü büyüt ve ortala

    # Bağlantı noktalarını çiz
    for edge in edges:
        pygame.draw.line(screen, (0, 0, 0), projected_vertices[edge[0]][:2], projected_vertices[edge[1]][:2], 2)

    # Ekranı güncelle
    pygame.display.flip()

    # FPS ayarı
    clock.tick(60)

    # Açıları güncelle
    theta_x += 0.02
    theta_y += 0.02
    theta_z += 0.02
import os
import pygame

def load_image(name):

    path = os.path.join('assets/png', f"{name}.png")
    image = pygame.image.load(path)
    rescaled_image = pygame.transform.scale(image, (80, 80))
    return rescaled_image
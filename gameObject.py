import pygame


class GameObject:

    def __init__(self, x, y, width, height, image_path):
        # Loading the image from the image path
        image = pygame.image.load(image_path)
        # Scaling the image to the size we want for it
        self.image = pygame.transform.scale(image, (width, height))
        # Saving the parameters as properties of the class objects
        self.x = x
        self.y = y
        self.width = width
        self.height = height

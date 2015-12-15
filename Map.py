import numpy, pygame
from PIL import Image

class Map:
    def __init__(self,size_node):
        self.image = Image.open('map.jpg')
        matrix = numpy.array(self.image)
        self.matrix = numpy.zeros(self.image.size)
        for x in range(matrix.shape[0]):
            for y in range(matrix.shape[1]):
                if matrix[x][y].all() != 255:
                    self.matrix[y][x] = 1
        self.MAPLayer = pygame.image.load('map.jpg')

    def get_layer(self):
        
        return self.MAPLayer

asd = Map(16)
print(asd.matrix)

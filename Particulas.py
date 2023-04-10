# import pygame
# import random
# import math

# # definir colores
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# RED = (0, 0, 0)

# # definir clase Partícula
# class Particle:
#     def __init__(self, x, y, size):
#         self.x = x
#         self.y = y
#         self.size = size
#         self.color = RED
#         self.thickness = 1
#         self.speed = random.randint(1, 1)
#         self.angle = random.randint(0, 360)
    
#     def move(self):
#         # actualizar posición basada en velocidad y ángulo
#         self.x += self.speed * math.cos(self.angle)
#         self.y += self.speed * math.sin(self.angle)
        
#         # comprobar si la partícula está fuera de la pantalla
#         if self.x < 0:
#             self.x = 800
#         elif self.x > 800:
#             self.x = 0
#         if self.y < 0:
#             self.y = 600
#         elif self.y > 600:
#             self.y = 0
            
#     def draw(self, screen):
#         # dibujar la partícula en la pantalla
#         pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size, self.thickness)

# # inicializar Pygame
# pygame.init()

# # establecer tamaño de pantalla
# size = (800, 600)
# screen = pygame.display.set_mode(size)

# # establecer título de la ventana
# pygame.display.set_caption("Simulación de partículas")

# # crear una lista de partículas
# particle_list = []
# for i in range(100):
#     x = random.randint(0, 800)
#     y = random.randint(0, 600)
#     size = random.randint(5, 10)
#     particle = Particle(x, y, size)
#     particle_list.append(particle)

# # establecer el reloj
# clock = pygame.time.Clock()

# # bucle principal del juego
# done = False
# while not done:
#     # manejar eventos
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
    
#     # limpiar la pantalla
#     screen.fill(WHITE)
    
#     # mover y dibujar todas las partículas
#     for particle in particle_list:
#         particle.move()
#         particle.draw(screen)
    
#     # actualizar la pantalla
#     pygame.display.flip()
    
#     # establecer límite de fotogramas
#     clock.tick(60)

# # cerrar Pygame
# pygame.quit()



import pygame
import random
import math

# definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# definir clase Partícula
class Particle:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = WHITE
        self.thickness = 0
        self.speed = random.randint(1, 2)
        self.angle = random.uniform(0, 2*math.pi)
    
    def move(self):
        # actualizar posición basada en velocidad y ángulo
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
        
        # comprobar si la partícula está fuera de la pantalla
        if self.x < 0:
            self.x = 800
        elif self.x > 800:
            self.x = 0
        if self.y < 0:
            self.y = 600
        elif self.y > 600:
            self.y = 0
    
    def draw(self, screen):
        # dibujar la partícula en la pantalla
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size, self.thickness)
        
    def repel(self, mouse_pos):
        # calcular distancia entre la partícula y el cursor del mouse
        dx = self.x - mouse_pos[0]
        dy = self.y - mouse_pos[1]
        dist = math.sqrt(dx**2 + dy**2)
        
        # si el cursor está cerca, repeler la partícula
        if dist < 50:
            angle = math.atan2(dy, dx)
            self.angle = angle + math.pi
        
# inicializar Pygame
pygame.init()

# establecer tamaño de pantalla
size = (1000, 800)
screen = pygame.display.set_mode(size)

# establecer título de la ventana
pygame.display.set_caption("Simulación de partículas")

# crear una lista de partículas
particle_list = []
for i in range(100):
    x = random.randint(0, 800)
    y = random.randint(0, 800)
    size = random.randint(3, 7)
    particle = Particle(x, y, size)
    particle_list.append(particle)

# establecer el reloj
clock = pygame.time.Clock()

# bucle principal del juego
done = False
while not done:
    # manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # obtener posición del cursor del mouse
    mouse_pos = pygame.mouse.get_pos()
    
    # limpiar la pantalla
    screen.fill(BLACK)
    
    # mover y dibujar todas las partículas
    for particle in particle_list:
        particle.move()
        particle.draw(screen)
        particle.repel(mouse_pos)
    
    # actualizar la pantalla
    pygame.display.flip()
    
    # establecer límite de fotogramas
    clock.tick(60)

# cerrar Pygame
pygame.quit()

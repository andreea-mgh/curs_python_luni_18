import pygame
import random as rand
import math

SCREEN_W = 800
SCREEN_H = 600

COLORS = {
    "BG": (0, 100, 150),
    "GROUND": (0, 128, 0),
    "PLAYER": (120, 100, 255),
    "PROJ": (255, 255, 0)
}

GROUND_Y = 500



class Player:
    def __init__(self, x, y):
        self.width = 40
        self.height = 60
        self.x = x
        self.y = y

        self.on_ground = True
        self.speed_y = 0

    def draw(self):
        pygame.draw.rect(screen, COLORS["PLAYER"], (self.x, self.y, self.width, self.height))

    def move(self, direction):
        if direction == "left":
            self.x -= 5
        elif direction == "right":
            self.x += 5
    
    def jump(self):
        if self.on_ground:
            self.speed_y = -15
            self.on_ground = False
    
    def update(self):
        self.y += self.speed_y
        self.speed_y += 0.8

        if self.y + self.height >= GROUND_Y:
            self.y = GROUND_Y - self.height
            self.on_ground = True
            self.speed_y = 0

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Bird:
    def __init__(self):
        self.width = 70
        self.height = 30
        self.y = -50
        self.x = rand.randint(0, SCREEN_W)
    
    def draw(self):
        pygame.draw.rect(screen, (0,0,0), (self.x, self.y, self.width, self.height))
    
    def update(self, player_x, player_y):
        dx = player_x - self.x
        dy = player_y - self.y
        angle = math.atan2(dy, dx) # calculeaza unghiul in functie de diferenta dintre 2 coord
        speed = 1.5
        self.x += speed * math.cos(angle)
        self.y += speed * math.sin(angle)
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Projectile:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.width = 15
        self.height = 8
        self.direction = d

    def draw(self):
        pygame.draw.rect(screen, COLORS["PROJ"], (self.x, self.y, self.width, self.height))
    
    def update(self):
        self.x += self.direction * 8
        if self.x < 0 or self.x > SCREEN_W:
            proj_list.remove(self)
      
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))

running = True

p = Player(300, 440)
birds_list = []
proj_list = []

SPAWN_BIRD_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_BIRD_EVENT, 5000)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == SPAWN_BIRD_EVENT:
            birds_list.append(Bird())
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            if mx < p.x:
                proj_list.append(Projectile(p.x, p.y, -1))
            else:
                proj_list.append(Projectile(p.x, p.y, 1))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            p.move("left")
        if keys[pygame.K_d]:
            p.move("right")
        if keys[pygame.K_SPACE]:
            p.jump()
        
    p.update()
    for b in birds_list:
        b.update(p.x, p.y)
        if b.get_rect().colliderect(p.get_rect()):
            running=False
        for pr in proj_list:
            if b.get_rect().colliderect(pr.get_rect()):
                birds_list.remove(b)
                proj_list.remove(pr)
    for pr in proj_list:
        pr.update()

    # --- SCREEN UPDATE ---

    screen.fill(COLORS["BG"])
    pygame.draw.rect(screen, COLORS["GROUND"], 
                    (0, GROUND_Y, SCREEN_W, SCREEN_H-GROUND_Y))
    
    p.draw()
    for b in birds_list:
        b.draw()
    for pr in proj_list:
        pr.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
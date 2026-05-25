import pygame
import random as rand

SCREEN_W = 800
SCREEN_H = 600

COLORS = {
    "BG": (0, 100, 150),
    "GROUND": (0, 128, 0),
    "PLAYER": (120, 100, 255)
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

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))

running = True

p = Player(300, 440)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
        #     p.move("left")
        
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
        #     p.move("right")

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            p.move("left")
        if keys[pygame.K_d]:
            p.move("right")
        if keys[pygame.K_SPACE]:
            p.jump()
        
    p.update()

    # --- SCREEN UPDATE ---

    screen.fill(COLORS["BG"])
    pygame.draw.rect(screen, COLORS["GROUND"], 
                    (0, GROUND_Y, SCREEN_W, SCREEN_H-GROUND_Y))
    
    p.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
import pygame

class MazeGame:
    def __init__(self):
        pygame.init()

        # Display constants
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 440
        self.WINDOW_TITLE = "Maze Game"

        # Colors
        self.BACKGROUND_COLOR = (180, 100, 255) 
        self.PLAYER_COLOR = (255, 255, 0)
        self.WALL_COLOR = (0, 255, 0)
        self.GOAL_COLOR = (255, 0, 0)

        # Maze layout
        self.maze = [
            "WWWWWWWWWWWWWWWWWWWW",
            "W        W         W",
            "W  WWWW  W  WWWWWW W",
            "W  W             W W",
            "W  W WWWWWWWWWW  W W",
            "W  W      W      W W",
            "W  WWWWWW WWWWWW W W",
            "W  W     W      W  W",
            "W  WWWW  WWWW  WWW W",
            "W        W          ",
            "WWWWWWWWWWWWWWWWWWWW",
        ]

        self.w = len(self.maze[0])
        self.h = len(self.maze)

        self.cell_size = self.WINDOW_HEIGHT / self.h

        self.create_wall()

        # PLAYER
        self.player_x = self.cell_size
        self.player_y = self.cell_size

        # GOAL
        self.goal_x = self.cell_size * 19
        self.goal_y = self.cell_size * 9



        self.running = True

        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption(self.WINDOW_TITLE)

    def create_wall(self):
        self.wall_blocks = []
        wall_size = self.cell_size
        for row_index, row in enumerate(self.maze):
            for col_index, cell in enumerate(row):
                if cell == 'W':
                    wall_block = pygame.Rect(col_index*wall_size, row_index*wall_size,
                                             wall_size, wall_size)
                    self.wall_blocks.append(wall_block)
        
    def run(self):
        while self.running:
            
            keys = pygame.key.get_pressed()
            speed = 0.4
            if keys[pygame.K_RIGHT]:  # sau K_d pentru WASD
                new_x = self.player_x + speed
                self.player_x = new_x


            self.window.fill(self.BACKGROUND_COLOR)

            # desenam peretii
            for cell in self.wall_blocks:
                pygame.draw.rect(self.window, self.WALL_COLOR, cell)

            #desenam player
            pygame.draw.rect(self.window, self.PLAYER_COLOR,
                            (self.player_x, self.player_y, self.cell_size, self.cell_size))
            # dezenam goal
            pygame.draw.rect(self.window, self.GOAL_COLOR,
                            (self.goal_x, self.goal_y, self.cell_size, self.cell_size))



            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

        pygame.quit()

if __name__ == "__main__":
    game = MazeGame()
    game.run()

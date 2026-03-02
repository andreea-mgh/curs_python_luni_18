import pygame

class MazeGame:
    def __init__(self):
        pygame.init()

        # Display constants
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 440
        self.WINDOW_TITLE = "Maze Game"

        # Colors
        self.BACKGROUND_COLOR = (0, 0, 128)
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

        self.running = True

        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption(self.WINDOW_TITLE)


    def run(self):
        while self.running:
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    game = MazeGame()
    game.run()

import pygame
import random
import numpy as np


class ClickableSquare(pygame.sprite.Sprite):
    def __init__(self, x, y, size, font, callback):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((255, 255, 255))  
        pygame.draw.rect(self.image, (0, 0, 0), self.image.get_rect(), 1)  
        self.rect = self.image.get_rect(topleft=(x, y))
        self.callback = callback
        self.font = font
        self.text = ""  

    def set_text(self, text):
        """Ustawia tekst w kwadracie."""
        self.text = text
        self.image.fill((255, 255, 255))  
        pygame.draw.rect(self.image, (0, 0, 0), self.image.get_rect(), 1)  
        if text:
            text_surface = self.font.render(text, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=self.image.get_rect().center)
            self.image.blit(text_surface, text_rect)

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    self.callback(self)



def on_click(square):
    """Callback, który ustawia losowy znak na klikniętym kwadracie."""
    global available_titles
    if available_titles:

        square.set_text(available_titles.pop(0))


def create_board(board_size, square_size, font, callback):
    """Tworzy planszę jako grupę sprite'ów."""
    board = pygame.sprite.Group()
    for row in range(board_size):
        for col in range(board_size):
            x = col * square_size
            y = row * square_size
            square = ClickableSquare(x, y, square_size, font, callback)
            board.add(square)
    return board


pygame.init()


WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FOX Game")
font = pygame.font.Font(None, 72)


board_size = 4
square_size = WIDTH // board_size


available_titles = ['F', 'X', 'O'] * 5
available_titles.append('O')
random.shuffle(available_titles)


board = create_board(board_size, square_size, font, on_click)
board_log=np.zeros((board_size, board_size), dtype=object)



running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    
    board.update(events)

  
    screen.fill((200, 200, 200))
    board.draw(screen)

    pygame.display.update()

pygame.quit()

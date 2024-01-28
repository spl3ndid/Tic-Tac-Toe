import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_COLOR = (0, 0, 0)
LINE_WIDTH = 15
WHITE = (255, 255, 255)

# Set up the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Define the game board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Function to draw the grid
def draw_grid():
    for i in range(1, 3):
        pygame.draw.line(window, LINE_COLOR, (i * WIDTH // 3, 0), (i * WIDTH // 3, HEIGHT), LINE_WIDTH)
        pygame.draw.line(window, LINE_COLOR, (0, i * HEIGHT // 3), (WIDTH, i * HEIGHT // 3), LINE_WIDTH)

# Function to draw X and O
def draw_xo(row, col):
    center_x = col * WIDTH // 3 + WIDTH // 6
    center_y = row * HEIGHT // 3 + HEIGHT // 6

    if board[row][col] == 'X':
        pygame.draw.line(window, LINE_COLOR, (center_x - 50, center_y - 50), (center_x + 50, center_y + 50), LINE_WIDTH)
        pygame.draw.line(window, LINE_COLOR, (center_x + 50, center_y - 50), (center_x - 50, center_y + 50), LINE_WIDTH)
    elif board[row][col] == 'O':
        pygame.draw.circle(window, LINE_COLOR, (center_x, center_y), 50, LINE_WIDTH)

# Function to check for a winner
def check_winner(player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Function to update the game state
def update_game_state():
    window.fill(WHITE)  # Fill the background with white color
    draw_grid()
    for row in range(3):
        for col in range(3):
            draw_xo(row, col)
    pygame.display.update()  # Update the display

# Main game loop
current_player = 'X'
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            col = int(event.pos[0] // (WIDTH // 3))
            row = int(event.pos[1] // (HEIGHT // 3))

            if board[row][col] == ' ':
                board[row][col] = current_player

                if check_winner(current_player):
                    print(f"Player {current_player} wins!")
                    running = False
                elif all(board[i][j] != ' ' for i in range(3) for j in range(3)):
                    print("It's a tie!")
                    running = False

                current_player = 'O' if current_player == 'X' else 'X'

    update_game_state()

# Quit Pygame
pygame.quit()
sys.exit()

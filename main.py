import pygame
import requests
import numpy as np
from sudoku_game import *
from candidate import Candidate

difficulty = ["easy", "medium", "hard", "random"]
random = np.random.randint(3)
choice = difficulty[random]
link = "https://sugoku.herokuapp.com/board?difficulty=" + choice
print(link)
response = requests.get(link)
print(link)
grid = response.json()['board']
grid_original = [
    [grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))
]


class Board:

    WIDTH = 550
    background_color = (251, 247, 245)
    original_grid_element_color = (52, 31, 151)
    buffer = 5

    # create display window
    SCREEN_HEIGHT = 500
    SCREEN_WIDTH = 80


def main():
    pygame.init()
    board = Board()
    win = pygame.display.set_mode((board.WIDTH, board.WIDTH))
    pygame.display.set_caption("Sudoku")
    win.fill(board.background_color)
    font = pygame.font.SysFont('Comic Sans MS', 35)

    for i in range(0, 10):
        if i % 3 == 0:
            # Y - Coord
            pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50),
                             (50 + 50 * i, 500), 4)
            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i),
                             (500, 50 + 50 * i), 4)
        # X - Coord
        pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50),
                         (50 + 50 * i, 500), 2)
        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i),
                         (500, 50 + 50 * i), 2)
    pygame.display.update()

    # Insertion of Random Numbers in the grid
    a_list = []
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            a_list.append(grid[i][j])
            # print(str(a_list) + ' lists')
            if 0 < grid[i][j] < 10:
                # print(str(grid[i]) + ' grids')
                # print(str(grid[j]) + ' gridz')
                # print(str(grid[i][j]) + 'grid')
                value = font.render(
                    str(grid[i][j]
                        ), True, board.original_grid_element_color
                )
                win.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))
    pygame.display.update() 

    print(a_list)
    sud_str = " ".join(map(str, a_list))
    print(sud_str)
    
    list = [a_list[i:i + 9] for i in range(0, len(a_list), 9)]
    # list = np.array(list)
    # print(" ".join(map(str, list)))
    # print(list)  # print the list of lists so that we can see the grid


    sudoku = Sudoku(list)
    print('Welcome to Python!')
    solution = sudoku.solve(list)

    i = 0
    while solution is None:
        i += 1
        print(f'Solution {i}: Restarting!')
        solution = sudoku.solve(list)
    print(f'Solution {i}: Solution Found!')
 
    while True:
        for event in pygame.event.get():
            # Just to Display Coordinates
            pos = pygame.mouse.get_pos()
            # print(pos)
            if event.type == pygame.QUIT:
                pygame.quit()
                return


if __name__ == "__main__":
    main()



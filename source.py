import pygame
import sys
import random
import math


class Hexagon:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.color = None
        self.neighbors = []


def hexa_grid(rows, cols):
    grid = [[Hexagon(row, col) for col in range(cols)] for row in range(rows)]
    return grid


def colors(grid, colors):
    for row in grid:
        for hexagon in row:

            colors_pos = set(colors) - {neighbor.color for neighbor in hexagon.neighbors}


            hexagon.color = random.choice(list(colors_pos))


def connect(grid):
    rows, cols = len(grid), len(grid[0])

    for row in range(rows):
        for col in range(cols):
            hexagon = grid[row][col]


            neighbor_offsets = [(0, 1), (1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1)]

            for offset in neighbor_offsets:
                neighbor_row, neighbor_col = row + offset[0], col + offset[1]

                if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                    hexagon.neighbors.append(grid[neighbor_row][neighbor_col])


def generate_hexa_grid(rows, cols, hex_size, offset_x, offset_y):
    grid = [[Hexagon(row, col) for col in range(cols)] for row in range(rows)]


    for row in range(rows):
        for col in range(cols):
            x = col * (hex_size * 1.5)
            y = row * (hex_size * math.sqrt(3)) + (col % 2) * (hex_size * math.sqrt(3) / 2)
            hexagon = grid[row][col]
            hexagon.position = (x + offset_x, y + offset_y)

    return grid


def hexa_draw(screen, color, center, size):

    pygame.draw.polygon(screen, color, [
        (center[0] + size * math.cos(angle), center[1] + size * math.sin(angle))
        for angle in [0, 60, 120, 180, 240, 300]
    ])


def grid_draw(screen, grid, hex_size):
    for row in grid:
        for hexagon in row:
            hexa_draw(screen, hexagon.color, hexagon.position, hex_size)



def main():
    pygame.init()

    rows, cols = 5, 5
    colors = [(255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 255, 0)]
    hex_size = 30
    offset_x, offset_y = 50, 50

    grid = generate_hexa_grid(rows, cols, hex_size, offset_x, offset_y)
    connect(grid)
    colors(grid, colors)

    screen_size = (
        cols * hex_size * 3 // 2 + offset_x * 2,
        rows * hex_size * math.sqrt(3) + offset_y * 2
    )
    screen = pygame.display.set_mode(screen_size)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))
        grid_draw(screen, grid, hex_size)
        pygame.display.flip()

    pygame.quit()

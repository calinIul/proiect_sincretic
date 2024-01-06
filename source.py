import random


class Hexagon:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.color = None
        self.neighbors = []


def grid(rows, cols):
    grid = [[Hexagon(row, col) for col in range(cols)] for row in range(rows)]
    return grid


def colors(grid, colors):
    for row in grid:
        for hexagon in row:

            available_colors = set(colors) - {neighbor.color for neighbor in hexagon.neighbors}

            hexagon.color = random.choice(list(available_colors))


def connect(grid):
    rows, cols = len(grid), len(grid[0])

    for row in range(rows):
        for col in range(cols):
            hexagon = grid[row][col]

            # Define the neighbors of a hexagon in a hexagonal grid
            neighbor_offsets = [(0, 1), (1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1)]

            for offset in neighbor_offsets:
                neighbor_row, neighbor_col = row + offset[0], col + offset[1]

                if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                    hexagon.neighbors.append(grid[neighbor_row][neighbor_col])


rows, cols = 5, 5
colors = ["rosu", "albastru", "verde", "galben"]

grid = grid(rows, cols)
connect(grid)
colors(grid, colors)

for row in grid:
    for hexagon in row:
        print(f"Hexagon ({hexagon.row}, {hexagon.col}) - culoare: {hexagon.color}")

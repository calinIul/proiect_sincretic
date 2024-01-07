import random
import math
from typing import List
from typing import Tuple

import pygame
from hexagon import FlatTopHexagonTile
from hexagon import HexagonTile

used_colors = []


def get_random_colour(min_=150, max_=255) -> Tuple[int, ...]:

    return tuple(random.choices(list(range(min_, max_)), k=3))


def create_hexagon(position, radius=50, flat_top=False) -> HexagonTile:

    global used_colors

    class_ = FlatTopHexagonTile if flat_top else HexagonTile
    hexagon = class_(radius, position, colour=get_random_colour())

    neighbor_colors = [neighbor.colour for neighbor in hexagon.compute_neighbours([hexagon])]

    while True:
        new_color = get_random_colour()
        if new_color not in neighbor_colors and new_color not in used_colors:
            break

    hexagon.colour = new_color
    used_colors.append(new_color)

    return hexagon


def init_hexagons(center=None, n=50, flat_top=False) -> List[HexagonTile]:
    if center is None:
        screen_width, screen_height = pygame.display.get_surface().get_size()
        center_x, center_y = screen_width // 2, screen_height // 2
        center = create_hexagon(position=(center_x, center_y), flat_top=flat_top)

    hexagons = [center]
    added = 0
    i = 0

    for _ in range(n):
        if added == n:
            break
        x, y = center.position
        top = create_hexagon(position=(x, y - 2 * center.minimal_radius), flat_top=flat_top)
        bottom = create_hexagon(position=(x, y + 2 * center.minimal_radius), flat_top=flat_top)
        rbotoom = create_hexagon(position=(x + 3 * center.radius / 2, y + center.minimal_radius), flat_top=flat_top)
        rtop = create_hexagon(position=(x + 3 * center.radius / 2, y - center.minimal_radius), flat_top=flat_top)
        lbottom = create_hexagon(position=(x - 3 * center.radius / 2, y + center.minimal_radius), flat_top=flat_top)
        ltop = create_hexagon(position=(x - 3 * center.radius / 2, y - center.minimal_radius), flat_top=flat_top)

        to_add = [rbotoom, rtop, top, ltop, lbottom, bottom]

        for hexagon in to_add:
            if hexagon.position not in [h.position for h in hexagons]:
                hexagons.append(hexagon)
                added += 1

        center = to_add[i]
        i = (i + 1) % 6

    return hexagons



def render(screen, hexagons):

    screen.fill((0, 0, 0))
    for hexagon in hexagons:
        hexagon.render(screen)

    # mouse_pos = pygame.mouse.get_pos()
    # colliding_hexagons = [
    #     hexagon for hexagon in hexagons if hexagon.collide_with_point(mouse_pos)
    # ]
    # for hexagon in colliding_hexagons:
    #     for neighbour in hexagon.compute_neighbours(hexagons):
    #         neighbour.render_highlight(screen, border_colour=(100, 100, 100))
    #     hexagon.render_highlight(screen, border_colour=(0, 0, 0))
    pygame.display.flip()


def main():

    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    hexagons = init_hexagons(flat_top=True)
    terminated = False
    hexagon_index = 0

    while not terminated:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminated = True

        screen.fill((0, 0, 0))


        render(screen, hexagons[:hexagon_index + 1])
        clock.tick(5)
        pygame.display.flip()

        if hexagon_index < len(hexagons):
            hexagon_index += 1

        if hexagon_index == len(hexagons):
            pygame.time.delay(2000)

    pygame.display.quit()


if __name__ == "__main__":
    main()

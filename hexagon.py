from __future__ import annotations

import math
from dataclasses import dataclass
from typing import List
from typing import Tuple

import pygame


@dataclass
class HexagonTile:


    radius: float
    position: Tuple[float, float]
    colour: Tuple[int, ...]

    def __post_init__(self):
        self.vertices = self.compute_vertices()

    def compute_vertices(self) -> List[Tuple[float, float]]:

        x, y = self.position
        half_radius = self.radius / 2
        minimal_radius = self.minimal_radius
        return [
            (x, y),
            (x - minimal_radius, y + half_radius),
            (x - minimal_radius, y + 3 * half_radius),
            (x, y + 2 * self.radius),
            (x + minimal_radius, y + 3 * half_radius),
            (x + minimal_radius, y + half_radius),
            (x + minimal_radius, y - 3 * half_radius),

        ]

    def compute_neighbours(self, hexagons: List[HexagonTile]) -> List[HexagonTile]:

        return [hexagon for hexagon in hexagons if self.is_neighbour(hexagon)]



    def is_neighbour(self, hexagon: HexagonTile) -> bool:

        distance = math.dist(hexagon.centre, self.centre)
        return math.isclose(distance, 2 * self.minimal_radius, rel_tol=0.05)

    def render(self, screen) -> None:

        pygame.draw.polygon(screen, self.colour, self.vertices)


    @property
    def centre(self) -> Tuple[float, float]:

        x, y = self.position
        return (x, y + self.radius)

    @property
    def minimal_radius(self) -> float:

        return self.radius * math.cos(math.radians(30))


class FlatTopHexagonTile(HexagonTile):

    def compute_vertices(self) -> List[Tuple[float, float]]:

        # pylint: disable=invalid-name
        x, y = self.position
        half_radius = self.radius / 2
        minimal_radius = self.minimal_radius
        return [
            (x, y),
            (x - half_radius, y + minimal_radius),
            (x, y + 2 * minimal_radius),
            (x + self.radius, y + 2 * minimal_radius),
            (x + 3 * half_radius, y + minimal_radius),
            (x + self.radius, y),

        ]

    @property
    def centre(self) -> Tuple[float, float]:

        x, y = self.position
        return (x + self.radius / 2, y + self.minimal_radius)
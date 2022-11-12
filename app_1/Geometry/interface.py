"""
    Interface of game
"""
from typing import Any, Tuple

import pygame

from Utility import geometry as Geo

GREY = (120, 120, 120)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
LIGHTGREEN = (128, 255, 0)
screen = pygame.display.set_mode((500, 600))

dic = {
    0: 'RED',
    1: 'YELLOW',
    2: 'GREEN',
    3: 'CYAN',
    4: 'BLUE',
    5: 'MAGENTA',
    6: 'BLACK',
    7: 'WHITE',
    8: 'GREY',
}


def draw_mouse(point_2d: Geo.Point2D) -> None:
    """
    Mouse draw
    """

    x_size = 5
    y_size = 5

    location_and_size = (int(point_2d.X - x_size/3), int(point_2d.Y - y_size/3),
                         x_size, y_size)

    pygame.draw.rect(screen, BLACK, location_and_size)


def draw_background() -> None:
    """
    Draw background with color
    """

    for num_x_way in range(6):
        for num_y_way in range(6):
            y_way = 25 + num_y_way*100
            x_way = 25 + num_x_way*100
            pygame.draw.rect(screen,
                             dic[num_y_way],
                             (x_way, y_way, 50, 50))


def draw_reset() -> None:
    """
    Reset draw
    """
    screen.fill(GREY)


def draw_element(type_element: str,
                 color: Any,
                 size: Any,
                 location: Any) -> None:
    """_summary_

    Args:
        type_element (str): _description_
        color (Any): _description_
        size (Any): _description_
        location (Any): _description_
    """
    if type_element == "Circle":
        Circle(color, size, location).create_element()

    elif type_element == "Rectangle":
        Rectangle(color, size, location).create_element()

    elif type_element == "Line":
        Line(color, size, location).create_element()

    elif type_element == "HollowCircle":
        HollowCircle(color, size, location).create_element()

    elif type_element == "PolygonDefault":
        Polygon(color, size, location).create_default_element()

    elif type_element == "ImpressiveRectangleT1":
        Rectangle(color, size, location).create_impressive_element_type_1(LIGHTGREEN)

class BaseElement():
    """
    Base class for element
    """

    def __init__(self,
                 color: Any,
                 size: Any,
                 location: Any) -> None:
        self.color = color
        self.size = size
        self.location = location

    def handle_properties(self) -> str:
        """
        handle color of element
        """

        if not isinstance(self.color, int):
            return dic[6]

        return dic[self.color]

    def handle_location_and_size(self):
        """
        Handle location and size
        """

        x_size, y_size = self.size
        mouse_x, mouse_y = self.location

        location = (int(mouse_x - x_size/2), int(mouse_y - y_size/2))

        return (*location, x_size, y_size)

    def handle_location(self) -> Tuple[int, int]:
        """
        Handle location and size
        """

        return self.location


class Rectangle(BaseElement):
    """
    Some thing
    Args:
        BaseElement (_type_): _description_
    """

    def create_element(self) -> None:
        """
        Create rectangle

        Returns:
            _type_: _description_
        """

        color = self.handle_properties()

        location_and_size = self.handle_location_and_size()

        pygame.draw.rect(screen, color, location_and_size)

    def create_impressive_element_type_1(self, shadow_color: Any) -> None:
        """
        Create impressive rectangle

        Returns:
            _type_: _description_
        """
        color = self.handle_properties()

        width = 3

        first_point = self.location[0]-self.size[0]/2, self.location[1]+self.size[1]/2
        second_point = self.location[0]+self.size[0]/2, self.location[1]+self.size[1]/2
        third_point = self.location[0]+self.size[0]/2, self.location[1]-self.size[1]/2
        fourth_point = self.location[0]-self.size[0]/2, self.location[1]-self.size[1]/2

        fifth_point = (self.location[0]+self.size[0]/2) + width*2/5,\
                      (self.location[1]+self.size[1]/2) - width
        sixth_point = (self.location[0]+self.size[0]/2) + width*2/5,\
                      (self.location[1]-self.size[1]/2) - width*2/5
        seventh_point = (self.location[0]-self.size[0]/2) + width,\
                        (self.location[1]-self.size[1]/2) - width*2/5

        pygame.draw.line(screen, shadow_color, fifth_point, sixth_point, width)
        pygame.draw.line(screen, shadow_color, sixth_point, seventh_point, width)

        pygame.draw.line(screen, color, first_point, second_point, width)
        pygame.draw.line(screen, color, second_point, third_point, width)
        pygame.draw.line(screen, color, third_point, fourth_point, width)
        pygame.draw.line(screen, color, fourth_point, first_point, width)


class Circle(BaseElement):
    """
    Some thing
    Args:
        BaseElement (_type_): _description_
    """

    def create_element(self) -> None:
        """
        Create rectangle

        Returns:
            _type_: _description_
        """

        color = self.handle_properties()

        location = self.handle_location()
        radius = self.size

        pygame.draw.circle(screen, color, location, radius)


class HollowCircle(BaseElement):
    """
    Some thing
    Args:
        BaseElement (_type_): _description_
    """

    def create_element(self) -> None:
        """
        Create hollow circle

        Returns:
            _type_: _description_
        """

        color = self.handle_properties()

        location_and_size = self.handle_location_and_size()

        pygame.draw.arc(screen, color, location_and_size,
                        start_angle=0, stop_angle=360)


class Line(BaseElement):
    """
    Some thing
    Args:
        BaseElement (_type_): _description_
    """

    def create_element(self) -> None:
        """
        Create Line 2D

        Returns:
            _type_: _description_
        """

        color = self.handle_properties()

        first_point, second_point = self.size

        pygame.draw.line(screen, color, first_point, second_point, width=3)


class Polygon(BaseElement):
    """
    Some thing
    Args:
        BaseElement (_type_): _description_
    """

    def create_element(self) -> None:
        """
        Create polygon

        Returns:
            _type_: _description_
        """

        color = self.handle_properties()

        location_and_size = self.handle_location_and_size()

        pygame.draw.polygon(screen, color, (location_and_size, (0, 0)))

    def create_default_element(self) -> None:
        """
        Create defaultpolygon

        Returns:
            _type_: _description_
        """

        color = self.handle_properties()

        location = self.handle_location()

        pygame.draw.polygon(screen, color, (location, (0, 0), (15, 60)))

"""
    Mode of game
"""
from typing import Any, List, Optional, Tuple
# from shapely.geometry import Point
import pygame

from Utility import geometry as Geo

pygame.mixer.init()
pygame.mixer.music.load(r"Sound\I Do - 911.mp3")

def event_control(location_mouse: Geo.Point2D,
                  mode_data: Any,
                  save_data: List[Any])\
        -> Tuple[bool, Any, Any, List[Any]]:
    """_summary_

    Args:
        location_mouse (Geo.Point2D): location_mouse in clude x value and y value
        mode_data (Any): Mode of element include
                         (type element, color, size, location)
        save_data (List[Any]): _description_

    Returns:
        Tuple[bool, Any, Any]: _description_
    """

    running = True
    data = None

    def event_button(mode_data: Any,
                     data: Optional[Any],
                     save_data: List[Any]):
        if mode_data is None:
            pygame.mixer.music.play()

            data = ("Circle", 0, 10,
                    (location_mouse.X, location_mouse.Y))
            mode_data = ("first", (location_mouse.X, location_mouse.Y))
            if save_data is not None:
                save_data.append((location_mouse.X, location_mouse.Y))

        elif mode_data[0] == "first":
            pygame.mixer.music.pause()

            data = (
                "Line", 1, (mode_data[1], (location_mouse.X, location_mouse.Y)), None)
            mode_data = (
                "second", (location_mouse.X, location_mouse.Y))
            if save_data is not None:
                save_data.append((location_mouse.X, location_mouse.Y))

        elif mode_data[0] == "second":
            pygame.mixer.music.unpause()

            data = ("Rectangle", 2, (50, 50),
                    (location_mouse.X, location_mouse.Y))
            mode_data = ("third", (location_mouse.X, location_mouse.Y))
            if save_data is not None:
                save_data.append((location_mouse.X, location_mouse.Y))

        elif mode_data[0] == "third":
            pygame.mixer.music.stop()

            data = ("HollowCircle", 3, (50, 50),
                    (location_mouse.X, location_mouse.Y))
            mode_data = (
                "fourth", (location_mouse.X, location_mouse.Y))
            if save_data is not None:
                save_data.append((location_mouse.X, location_mouse.Y))

        elif mode_data[0] == "fourth":
            data = ("ImpressiveRectangleT1", 2, (50, 50),
                    (location_mouse.X, location_mouse.Y))

            mode_data = (
                "fifth", (location_mouse.X, location_mouse.Y))
            if save_data is not None:
                save_data.append((location_mouse.X, location_mouse.Y))

        elif mode_data[0] == "fifth":
            data = ("PolygonDefault", 4, (50, 50),
                    (location_mouse.X, location_mouse.Y))
            mode_data = None
            # Reset the list save data
            del save_data[:]

        return data, mode_data, save_data

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button:

                data, mode_data, save_data = event_button(
                    mode_data, data, save_data)

    return running, data, mode_data, save_data

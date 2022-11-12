"""
This is main module
"""

from typing import Any, Optional

import pygame

from EventStage import button_mode
from Geometry import interface
from Utility import geometry as Geo

pygame.init()

running = True


class Main():
    """
    class execution
    """

    def __init__(self,
                 building_data: Optional[Any],
                 mode_data: Optional[Any]) -> None:
        self.running = True
        self.building_data = building_data
        self.mode_data = mode_data

    def execution(self):
        """
        Execute create sketch
        """

        location_mouse = pygame.mouse.get_pos()
        location_mouse = Geo.Point2D(location_mouse)

        interface.draw_reset()

        interface.draw_background()

        interface.draw_mouse(location_mouse)

        if self.building_data is not None:
            interface.draw_element(*self.building_data)  # type: ignore

        save_data = []  # test
        self.running, building_data, self.mode_data, save_data\
            = button_mode.event_control(location_mouse, self.mode_data, save_data)

        if building_data is not None:
            self.building_data = building_data

        pygame.display.flip()

        return self.running, self.building_data, self.mode_data

    def some_thing(self) -> None:
        """Do some thing
        """


building_data = None
mode_data = None

while running:  # Main loop
    running, building_data, mode_data = Main(
        building_data, mode_data).execution()

pygame.quit()

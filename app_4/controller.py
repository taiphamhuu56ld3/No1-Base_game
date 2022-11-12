"""
Try using Model-View-Controller
"""

import sys
from typing import Any, Dict, List

import pygame
from pygame.rect import Rect
from pygame.surface import Surface

from controlChildren import sound, time
from Model.model import ModelBasic
from View import view

pygame.init()

GRAVITY = 4
MAX_SCREEN_X = 1200
MAX_SCREEN_Y = 600
MAN_HIGH = 200/2
MAN_WIDTH = 100/2
high_score = 0#
score = 0#
score_sound_count_down = sound.SCORE_SOUND_COUND_DOWN#

floor_x_pos = 0#

game_active = True#

pip_surface = view.pip_surface#
pipe_list = view.pipe_list#

man_movement = 0#
man_jump = time.man_jump
man_run_list = view.man_run_list#
man_index = view.MAN_INDEX#
man_run = view.man_run#
man_y_pos = 0#

spawnpip = time.spawnpip


my_items :List[Dict[str, Any]] = [
    {'name': 'high_score', 'value': 0},
    {'name': 'score', 'value': 0},
    {'name': 'score_sound_count_down', 'value': sound.SCORE_SOUND_COUND_DOWN},
    {'name': 'floor_x_pos', 'value': 0},
    {'name': 'game_active', 'value': True},
    {'name': 'running', 'value': True},
    {'name': 'pip_surface', 'value': view.pip_surface},
    {'name': 'pipe_list', 'value': view.pipe_list},
    {'name': 'man_movement', 'value': 0},
    {'name': 'man_run_list', 'value': view.man_run_list},
    {'name': 'man_index', 'value': view.MAN_INDEX},
    {'name': 'man_run', 'value': view.man_run},
    {'name': 'man_y_pos', 'value': 0},
    ]


class Controller():
    """
    Description for controller
    """

    def __init__(self, module: ModelBasic):
        self.module = module

    def execution(self):
        """
        Controller execution
        """
        _floor_x_pos = self.module.value.floor_x_pos
        _man_y_pos = self.module.value.man.y_pos
        _running = self.module.value.running
        _man_movement = self.module.value.man.movement
        _pipe_list = self.module.value.pip.list
        _pip_surface = self.module.value.pip.surface
        _game_active = self.module.value.game_active
        _man_index = self.module.value.man.index
        _man_run = self.module.value.man.run
        _score = self.module.value.score.score
        _high_score = self.module.value.score.high_score
        _man_run_list = self.module.value.man.list
        _score_sound_count_down = self.module.value.score.score_sound_count_down

        # Location
        man_run_rec = _man_run.get_rect(center=(MAN_WIDTH*2, MAN_HIGH))

        man_movement_up = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sound.soundtrack.stop()
                _running = False


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if _game_active:
                        man_movement_up = -(GRAVITY * 25)
                        sound.flap_sound.play()
                    else:
                        _game_active = True
                        _pipe_list.clear()
                        man_run_rec.center = (int(MAN_WIDTH), int(MAN_HIGH))
                        _man_movement = 0
                        _score = 0
                        sound.soundtrack.unpause()

            if event.type == spawnpip:
                _pipe_list.extend(view.create_pipe(_pip_surface))

            if event.type == man_jump:
                if _man_index < 2:
                    _man_index += 1
                else:
                    _man_index = 0

                _man_run, man_run_rec = view.man_animation(
                    man_run_rec, _man_run_list, _man_index)

        view.background()
        if _game_active:

            _man_y_pos += 1
            _man_movement += GRAVITY + man_movement_up
            man_run_rec.centery += _man_movement  # type: ignore

            rotated_man = self.__rotated_man(_man_run, _man_movement)

            # Resize
            man_run_rec.size = int(MAN_WIDTH), int(MAN_HIGH)
            view.draw_man_rotated(rotated_man, man_run_rec)
            _game_active = self.__check_collision(_pipe_list, man_run_rec)
            # Pipe
            _pipe_list = view.move_pipe(_pipe_list)
            view.draw_pipe(_pipe_list, _pip_surface)
            _score += 0.02
            view.score_display(_score, "main_game", _high_score)
            _score_sound_count_down -= 1
            if _score_sound_count_down <= 0:
                sound.score_sound.play()
                _score_sound_count_down = sound.SCORE_SOUND_COUND_DOWN
        else:
            view.create_end_screen()
            _high_score = self.__update_score(_score, _high_score)
            view.score_display(_score, "game_over", _high_score)
            sound.soundtrack.pause()

        # floor
        _floor_x_pos -= 1
        _floor_x_pos = view.draw_floor(_floor_x_pos)

        if _floor_x_pos <= -MAX_SCREEN_X:
            _floor_x_pos = 0.

        if _man_y_pos >= MAX_SCREEN_Y:
            _man_y_pos = 0.

        pygame.display.update()
        time.clock.tick(60)

        return self.model

    def __check_collision(self, pipes: List[Rect], man_run_rec: Rect)\
            -> bool:
        """ Check collision """
        for pipe in pipes:
            if man_run_rec.colliderect(pipe):
                sound.hit_sound.play()
                return False

        if man_run_rec.top <= -75\
                or man_run_rec.bottom >= MAX_SCREEN_Y:
            return False
        return True

    def __rotated_man(self, man: Surface, _man_movement: float) -> Surface:
        """ Rotate and resize """
        if _man_movement <= 0:
            angle = _man_movement*3
        elif _man_movement > 250:
            angle = -_man_movement*0.03
        else:
            angle = -_man_movement*0.06

        new_man = pygame.transform.rotozoom(man, angle, 0.5)
        return new_man

    def __update_score(self, _score: float, _high_score: float) -> float:
        """ Update score """
        if _score > _high_score:
            _high_score = _score
        return _high_score


while True:  # Main loop
    self_ = ModelBasic(my_items)

    main = Controller(self_)
    self_ = main.execution()
    running = self_.value.running

    if not running:
        pygame.quit()
        sys.exit()
        break

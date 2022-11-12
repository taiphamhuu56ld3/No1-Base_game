"""
The Model manages the data and defines rules and behaviors.
It represents the business logic of the application.
The data can be stored in the Model itself or in a database
(only the Model has access to the database).
"""
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union, cast


class ItemNotStored(Exception):
    pass


@dataclass
class Score():
    high_score: float = 0.
    score: float = 0.
    score_sound_count_down: float = 33.


@dataclass
class Pip():
    surface: float = 33.
    list: float = 60.


@dataclass
class Man():
    movement: float = 0.
    list: float = 622.
    index: int = 909
    run: int = 15
    y_pos: float = 0


@dataclass
class ElementValue:
    floor_x_pos: float = 0.
    game_active: bool = True
    running: bool = True
    score: Score = Any
    pip: Pip = Any
    man: Man = Any


class ModelBasic:

    def __init__(self, my_items: Optional[List[Dict[str, Any]]] = None) -> None:

        if my_items is None:
            self.value = ElementValue()

        else:
            (floor_x_pos, game_active, running, high_score,
            score, score_sound_count_down, pipe_list,
            pip_surface, man_movement, man_run_list, man_index,
            man_run, man_y_pos) = self._rearrange(my_items)

            self.value = ElementValue(
                floor_x_pos=floor_x_pos,
                game_active=game_active,
                running=running,
                score=Score(
                high_score=high_score,
                score=score,
                score_sound_count_down=score_sound_count_down),
                pip=Pip(
                surface=pip_surface,
                list=pipe_list),
                man= Man(
                movement=man_movement,
                list=man_run_list,
                index=man_index,
                run=man_run,
                y_pos=man_y_pos)
            )

    def get_value(self,
                  name: str,
                  _iterms: List[Dict[str, Union[str, float, int]]]):
        return self._read_item(name, _iterms).get('value')

    def _read_item(self,
                  name: str,
                  _iterms: List[Dict[str, Union[str, float, int]]])\
            -> Dict[str, Union[str, float, int]]:
        myitems: List[Dict[str, Union[str, float, int]]]\
            = list(filter(lambda x: x['name'] == name, _iterms))

        if myitems:
            return myitems[0]

        raise ItemNotStored(
            f'Can\'t read "{name}" because it\'s not stored')

    def _rearrange(self, my_items: List[Dict[str, Any]]):
        floor_x_pos = self.get_value("floor_x_pos", my_items)
        floor_x_pos = cast(float, floor_x_pos)
        game_active = self.get_value("game_active", my_items)
        game_active = cast(bool, game_active)
        running = self.get_value("running", my_items)
        running = cast(bool, running)
        high_score = self.get_value("high_score", my_items)
        high_score = cast(float, high_score)
        score = self.get_value("score", my_items)
        score = cast(float, score)
        score_sound_count_down = self.get_value(
            "score_sound_count_down", my_items)
        score_sound_count_down = cast(float, score_sound_count_down)
        pip_surface = self.get_value("pip_surface", my_items)
        pip_surface = cast(float, pip_surface)
        pipe_list = self.get_value("pipe_list", my_items)
        pipe_list = cast(float, pipe_list)
        man_movement = self.get_value("man_movement", my_items)
        man_movement = cast(float, man_movement)
        man_run_list = self.get_value("man_run_list", my_items)
        man_run_list = cast(float, man_run_list)
        man_index = self.get_value("man_index", my_items)
        man_index = cast(int, man_index)
        man_run = self.get_value("man_run", my_items)
        man_run = cast(int, man_run)
        man_y_pos = self.get_value("man_y_pos", my_items)
        man_y_pos = cast(int, man_y_pos)

        return (floor_x_pos,
                game_active,
                running,
                high_score,
                score,
                score_sound_count_down,
                pipe_list,
                pip_surface,
                man_movement,
                man_run_list,
                man_index,
                man_run,
                man_y_pos,
                )

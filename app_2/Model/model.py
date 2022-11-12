"""
The Model manages the data and defines rules and behaviors.
It represents the business logic of the application.
The data can be stored in the Model itself or in a database
(only the Model has access to the database).
"""
from typing import Any, Dict, List, Union, Iterable

import mvc_exceptions as mvc_exc


class_something = [
    {"name": "high_score", "value": 0},
    {"name": "score", "value": 0},
    {"name": "score_sound_count_down", "value": 33},
    {"name": "floor_x_pos", "value": 0},
    {"name": "game_active", "value": True},
    {"name": "running", "value": True},
    {"name": "pip_surface", "value": 33},
    {"name": "pipe_list", "value": 60},
    {"name": "man_movement", "value": 0},
    {"name": "man_run_list", "value": 622},
    {"name": "man_index", "value": 909},
    {"name": "man_run", "value": 15},
    {"name": "man_y_pos", "value": 0}
    ]

class ElementValue():
    """_summary_
    """
    def __init__(self, name: str, value: Any) -> None:
        self.name = name
        self.value = value

class ListElementValue():
    """_summary_
    """
    def __init__(self, ):
        self.list_element_value: List[Any] = []

    def append(self, element_value: ElementValue) -> None:
        return self.list_element_value.append(element_value)

    def extend(self, element_values: Iterable[ElementValue]) -> None:
        return self.list_element_value.extend(element_values)

class Part1:
    """_summary_
    """
    def __init__(self, list_element_value: List[ElementValue]) -> None:
        self.list_element_value = list_element_value

    def __repr__(self) -> str:
        string = ''
        for element_value in self.list_element_value:
            string += str(str(element_value.name) + ': ' + str(element_value.value) + '\n')
        return f'list_element_value: {string}'

list_value: List[Any] = []
for i, item in enumerate(class_something):
    list_value.append(ElementValue(f'{item["name"]}', f'{item["value"]}'))

# print(Part1(list_value))
# a = Part1(list_value)
items: List[Dict[str, Any]] = []

class ModelBasic():
    """
    ModelBasic have CRUD

    """

    def __init__(self,
                 application_items: List[Dict[str, Union[str, float, int]]]):
        self.item_type = 'Using Model-View-Controller'
        self.create_items(application_items)

    def create_item(self, _name: str, _value: Any):
        ...

    def create_items(self,
                     app_items: List[Dict[str, Union[str, float, int]]]):
        global items
        items = app_items

    def read_item(self, _name: str) -> Dict[str, Union[str, float, int]]:
        global items
        myitems: List[Dict[str, Union[str, float, int]]]\
            = list(filter(lambda x: x['name'] == _name, items))
        if myitems:
            return myitems[0]

        raise mvc_exc.ItemNotStored(
            f'Can\'t read "{_name}" because it\'s not stored')

    def read_items(self) -> List[Dict[str, Union[str, float, int]]]:
        global items
        return list(item for item in items)

    def update_item(self, _name: str, value: Any):
        global items

        idxs_items: List[Any] = list(
            filter(lambda i_x: i_x[1]['name'] == _name, enumerate(items)))
        if idxs_items:
            _i, _item_to_update = idxs_items[0][0], idxs_items[0][1]
            items[_i] = {'name': _name, 'value': value}
        else:
            raise mvc_exc.ItemNotStored(
                f'Can\'t update "{_name}" because it\'s not stored')

    def delete_item(self, _name: str):
        global items
        idxs_items: List[Any] = list(
            filter(lambda i_x: i_x[1]['name'] == _name, enumerate(items)))
        if idxs_items:
            _i, _item_to_delete = idxs_items[0][0], idxs_items[0][1]
            del items[_i]
        else:
            raise mvc_exc.ItemNotStored(
                f'Can\'t delete "{_name}" because it\'s not stored')

    def get_value(self, name: str) -> Any:
        return self.read_item(name).get('value')

    def set_value(self, name: str, value: Any) -> None:
        return self.update_item(name, value)

# class dotdict(dict): # type: ignore
#     """dot.notation access to dictionary attributes"""
#     __getattr__: Any = dict.get # type: ignore
#     __setattr__ = dict.__setitem__ # type: ignore
#     __delattr__ = dict.__delitem__ # type: ignore

# build_ele = {'parameter':'it works'}
# nested_dict = {'value':'nested works too'}
# build_ele = dotdict(build_ele)
# # build_ele.parameter

# build_ele.nested = dotdict(nested_dict)

# print(build_ele.nested.value)
# print(build_ele.parameter)

# ##2
# from box import Box

# mydict = {"key1":{"v1":0.375,
#                     "v2":0.625},
#           "key2":0.125,
#           }
# mydict = Box(mydict)

# print(mydict.key1.v1)

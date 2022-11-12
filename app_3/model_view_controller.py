from typing import Any, List, Dict, Union
import basic_backend
import mvc_exceptions as mvc_exc


class ModelBasic():
    """The Model manages the data and defines rules and behaviors.
    It represents the business logic of the application.
    The data can be stored in the Model itself or in a database
    (only the Model has access to the database).
    """

    def __init__(self, application_items: List[Dict[str, Union[str, float, int]]]):
        self._item_type = 'product'
        self.create_items(application_items)

    @property
    def item_type(self) -> str:
        return self._item_type

    @item_type.setter
    def item_type(self, new_item_type: str):
        self._item_type = new_item_type

    def create_item(self, name: str, price: float, quantity: int):
        basic_backend.create_item(name, price, quantity)

    def create_items(self, items: List[Dict[str, Union[str, float, int]]]):
        basic_backend.create_items(items)

    def read_item(self, name: str) -> Dict[str, Union[str, float, int]]:
        return basic_backend.read_item(name)

    def read_items(self) -> List[Dict[str, Union[str, float, int]]]:
        return basic_backend.read_items()

    def update_item(self, name: str, price: Any, quantity: Any):
        basic_backend.update_item(name, price, quantity)

    def delete_item(self, name: str):
        basic_backend.delete_item(name)


class View():
    """The View presents the data to the user.
    A View can be any kind of output representation:
    a HTML page, a chart, a table, or even a simple text output.
    A View should never call its own methods; only a Controller should do it.
    """
    @staticmethod
    def show_bullet_point_list(item_type: str, items: List[Any]):
        print(f'--- {item_type.upper()} LIST ---')
        for item in items:
            print(f'* {item}')

    @staticmethod
    def show_number_point_list(item_type: str, items: List[Any]):
        print(f'--- {item_type.upper()} LIST ---')
        for i, item in enumerate(items):
            print(f'{i+1}. {item}')

    @staticmethod
    def show_item(item_type: str,
                  item: str,
                  item_info: Dict[str, Union[str, float, int]]):
        print('//////////////////////////////////////////////////////////////')
        print(f'Good news, we have some {item.upper()}!')
        print(f'{item_type.upper()} INFO: {item_info}')
        print('//////////////////////////////////////////////////////////////')

    @staticmethod
    def display_missing_item_error(item: str, err: mvc_exc.ItemNotStored):
        print('**************************************************************')
        print(f'We are sorry, we have no {item.upper()}!')
        print(f'{err.args[0]}')
        print('**************************************************************')

    @staticmethod
    def display_item_already_stored_error(item: str,
                                        item_type: str,
                                        err: mvc_exc.ItemAlreadyStored):
        print('**************************************************************')
        print(f'Hey! We already have {item.upper()} in our {item_type} list!'
              )
        print(f'{err.args[0]}')
        print('**************************************************************')

    @staticmethod
    def display_item_not_yet_stored_error(item: str,
                                        item_type: str,
                                        err: mvc_exc.ItemNotStored):
        print('**************************************************************')
        print(f'We don\'t have any {item.upper()} in our {item_type} list.'
                ' Please insert it first!'
              )
        print(f'{err.args[0]}')
        print('**************************************************************')

    @staticmethod
    def display_item_stored(item: str, item_type: str):
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print(f'Hooray! We have just added some {item.upper()} to our {item_type} list!'
              )
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    @staticmethod
    def display_change_item_type(older: Any, newer: Any):
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print(f'Change item type from "{older}" to "{newer}"')
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def display_item_updated(item: Any, o_price: Any, o_quantity:
                             Any, n_price: Any, n_quantity: Any):
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print(f'Change {item} price: {o_price} --> {n_price}'
              )
        print(f'Change {item} quantity: {o_quantity} --> {n_quantity}'
              )
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def display_item_deletion(name: Any):
        print('--------------------------------------------------------------')
        print(f'We have just removed {name} from our list')
        print('--------------------------------------------------------------')


class Controller():
    """The Controller accepts user's inputs
    and delegates data representation to a View
    and data handling to a Model.
    """

    def __init__(self, model: ModelBasic, view: View):
        self.model = model
        self.view = view

    def show_items(self, bullet_points: bool = False):
        items = self.model.read_items()
        item_type = self.model.item_type
        if bullet_points:
            self.view.show_bullet_point_list(item_type, items)
        else:
            self.view.show_number_point_list(item_type, items)

    def show_item(self, item_name: str):
        try:
            item = self.model.read_item(item_name)
            item_type = self.model.item_type
            self.view.show_item(item_type, item_name, item)
        except mvc_exc.ItemNotStored as e:
            self.view.display_missing_item_error(item_name, e)

    def insert_item(self, name: str, price: float, quantity: int):
        assert price > 0, 'price must be greater than 0'
        assert quantity >= 0, 'quantity must be greater than or equal to 0'
        item_type = self.model.item_type
        try:
            self.model.create_item(name, price, quantity)
            self.view.display_item_stored(name, item_type)
        except mvc_exc.ItemAlreadyStored as e:
            self.view.display_item_already_stored_error(name, item_type, e)

    def update_item(self, name: Any, price: float, quantity: int):
        assert price > 0, 'price must be greater than 0'
        assert quantity >= 0, 'quantity must be greater than or equal to 0'
        item_type = self.model.item_type

        try:
            older = self.model.read_item(name)
            self.model.update_item(name, price, quantity)
            self.view.display_item_updated(
                name, older['price'], older['quantity'], price, quantity)
        except mvc_exc.ItemNotStored as e:
            self.view.display_item_not_yet_stored_error(name, item_type, e)
            # if the item is not yet stored and we performed an update, we have
            # 2 options: do nothing or call insert_item to add it.
            # self.insert_item(name, price, quantity)

    def update_item_type(self, new_item_type: Any):
        old_item_type = self.model.item_type
        self.model.item_type = new_item_type
        self.view.display_change_item_type(old_item_type, new_item_type)

    def delete_item(self, name: str):
        item_type = self.model.item_type
        try:
            self.model.delete_item(name)
            self.view.display_item_deletion(name)
        except mvc_exc.ItemNotStored as e:
            self.view.display_item_not_yet_stored_error(name, item_type, e)


my_items = [
    {'name': 'bread', 'price': 0.5, 'quantity': 20},
    {'name': 'milk', 'price': 1.0, 'quantity': 10},
    {'name': 'wine', 'price': 10.0, 'quantity': 5},
]

c = Controller(ModelBasic(my_items), View())

c.show_items()

# c.show_items(bullet_points=True)

# c.show_item('chocolate')

# c.show_item('bread')

# c.insert_item('bread', price=1.0, quantity=5)

# c.insert_item('chocolate', price=2.0, quantity=10)

# c.show_item('chocolate')

# c.update_item('milk', price=1.2, quantity=20)

# c.delete_item('fish')

# c.delete_item('bread')

# c.show_item('bread')

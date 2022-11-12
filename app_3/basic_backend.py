
from typing import Any, List, Dict, Union
import mvc_exceptions as mvc_exc


items: List[Dict[str, Union[str, float, int]]] = []  # global variable where we keep the data


def create_items(app_items: List[Dict[str, Union[str, float, int]]])\
    -> None:
    global items
    items = app_items


def create_item(name: str, price: float, quantity: int) -> None:
    global items
    results: List[Dict[str, Union[str, float, int]]]\
                    = list(filter(lambda x: x['name'] == name, items))
    if results:
        raise mvc_exc.ItemAlreadyStored(f'"{name}" already stored!')

    items.append({'name': name, 'price': price, 'quantity': quantity})


def read_item(name: str) -> Dict[str, Union[str, float, int]]:
    global items
    myitems: List[Dict[str, Union[str, float, int]]]\
         = list(filter(lambda x: x['name'] == name, items))
    if myitems:
        return myitems[0]

    raise mvc_exc.ItemNotStored(
        f'Can\'t read "{name}" because it\'s not stored')


def read_items():
    global items
    return list(item for item in items)


def update_item(name: str, price: float, quantity: int):
    global items
    # Python 3.x removed tuple parameters unpacking (PEP 3113),
    # so we have to do it manually (i_x is a tuple, idxs_items is a list of tuples)
    idxs_items: List[Any] = list(
        filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))
    if idxs_items:
        i, _item_to_update = idxs_items[0][0], idxs_items[0][1]
        items[i] = {'name': name, 'price': price, 'quantity': quantity}
    else:
        raise mvc_exc.ItemNotStored(
            f'Can\'t update "{name}" because it\'s not stored')


def delete_item(name: str):
    global items
    # Python 3.x removed tuple parameters unpacking (PEP 3113),
    # so we have to do it manually (i_x is a tuple, idxs_items is a list of tuples)
    idxs_items: List[Any] = list(
        filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))
    if idxs_items:
        i, _item_to_delete = idxs_items[0][0], idxs_items[0][1]
        del items[i]
    else:
        raise mvc_exc.ItemNotStored(
            f'Can\'t delete "{name}" because it\'s not stored')


def main():

    my_items = [
        {'name': 'bread', 'price': 0.5, 'quantity': 20},
        {'name': 'milk', 'price': 1.0, 'quantity': 10},
        {'name': 'wine', 'price': 10.0, 'quantity': 5},
    ]

    # CREATE
    create_items(my_items)
    create_item('beer', price=3.0, quantity=15)
    # if we try to re-create an object we get an ItemAlreadyStored exception
    # create_item('beer', price=2.0, quantity=10)

    # READ
    print('READ items')
    print(read_items())
    # if we try to read an object not stored we get an ItemNotStored exception
    # print('READ chocolate')
    # print(read_item('chocolate'))
    print('READ bread')
    print(read_item('bread'))

    # UPDATE
    print('UPDATE bread')
    update_item('bread', price=2.0, quantity=30)
    print(read_item('bread'))
    # if we try to update an object not stored we get an ItemNotStored exception
    # print('UPDATE chocolate')
    # update_item('chocolate', price=10.0, quantity=20)

    # DELETE
    print('DELETE beer')
    delete_item('beer')
    # if we try to delete an object not stored we get an ItemNotStored exception
    # print('DELETE chocolate')
    # delete_item('chocolate')

    print('READ items')
    print(read_items())


if __name__ == '__main__':
    main()

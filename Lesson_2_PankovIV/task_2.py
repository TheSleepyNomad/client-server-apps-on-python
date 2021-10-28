"""
Задание №2
Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON
с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными.
Для этого:

    1) Создать функцию write_order_to_json(), в которую передается 5 параметров:
    товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date).
    Функция должна предусматривать запись данных в виде словаря в файл orders.json.
    При записи данных указать величину отступа в 4 пробельных символа;

    2) Проверить работу программы через вызов функции write_order_to_json()
    с передачей в нее значений каждого параметра.
"""

import json


def write_order_to_json(item, quantity, price, buyer, date):
    order = {'Товар': item,
             'Количество': quantity,
             'Цена': price,
             'Покупатель': buyer,
             'Дата': date, }
    with open('orders.json', 'r+', encoding='utf-8') as f_n:
        objs = json.load(f_n)
        objs['orders'].append(order)
        print(objs)
        f_n.seek(0)
        json.dump(objs, f_n, indent=4)


write_order_to_json('Компьютер', '1', '11500', 'Иванов И.И', '01.01.21')

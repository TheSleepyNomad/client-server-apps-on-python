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
from json.decoder import JSONDecodeError


def write_order_to_json(item, quantity, price, buyer, date):
    # Формируем запись о заказе
    order = {'Товар': item,
             'Количество': quantity,
             'Цена': price,
             'Покупатель': buyer,
             'Дата': date, }

    orders = {'orders': []}

    # Открываем файл на чтение
    with open('orders.json', 'r+', encoding='utf-8') as file_json:
        # Пробуем прочесть файл.
        try:
            data = json.load(file_json)
            data['orders'].append(order)
            file_json.seek(0)
            json.dump(data, file_json, indent=4, ensure_ascii=False)
        # На случай, если файл пустой
        except JSONDecodeError:
            print('Файл пустой. Запишем новые данные')
            file_json.seek(0)
            orders['orders'].append(order)
            json.dump(orders, file_json, indent=4, ensure_ascii=False)
            print('Готово')


if __name__ == '__main__':
    write_order_to_json('Компьютер', '1', '11500', 'Иванов И.И', '01.01.21')
    write_order_to_json('Машина', '1', '2400000', 'Петров В.Т', '01.01.21')
    write_order_to_json('Дом', '1', '5521540', 'Смиронов Ю.А', '01.01.21')

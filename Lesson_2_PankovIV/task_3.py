"""
Задание №3
Задание на закрепление знаний по модулю yaml.
Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата.
Для этого:

    1) Подготовить данные для записи в виде словаря, в котором первому ключу
    соответствует список, второму — целое число, третьему — вложенный словарь,
    где значение каждого ключа — это целое число с юникод-символом,
    отсутствующим в кодировке ASCII (например, €);

    2) Реализовать сохранение данных в файл формата YAML — например, в файл
    file.yaml. При этом обеспечить стилизацию файла с помощью параметра
    default_flow_style, а также установить возможность работы с юникодом:
    allow_unicode = True;

    3) Реализовать считывание данных из созданного файла и проверить,
    совпадают ли они с исходными.
"""
import yaml

data_for_file = {
    'first key': [1, 'word', 10.3, '\u0441\u043e\u043a\u0435\u0442'],
    'second key': 1984,
    'third key': {
        '1': '1 \u00b1',
        '2': '2 \u22cc',
        '3': '3 \u2031',
        '4': '4 \u221c',
        '5': '5 \u299d',
    }
}

if __name__ == '__main__':
    # Создаем и пишем данные в новый файл
    with open('data_write.yaml', 'w+', encoding='utf-8') as yaml_file:
        yaml.dump(data_for_file, yaml_file,
                  allow_unicode=True,
                  default_flow_style=False)
    # Читаем
    with open('data_write.yaml', 'r', encoding='utf-8') as yaml_file:
        data = yaml.safe_load(yaml_file)
        # Проверяем ключи и их значения
        if data.keys() == data_for_file.keys():
            print('Ключи совпадают')
            for key in data.keys():
                if data[key] == data_for_file[key]:
                    print('Значения совпадают')

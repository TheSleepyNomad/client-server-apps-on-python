"""
Задание №1

Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку
определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый
«отчетный» файл в формате CSV. Для этого:

    a) Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с
    данными, их открытие и считывание данных. В этой функции из считанных данных
    необходимо с помощью регулярных выражений извлечь значения параметров
    «Изготовитель системы»,  «Название ОС», «Код продукта», «Тип системы».
    Значения каждого параметра поместить в соответствующий список. Должно получиться
    четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
    В этой же функции создать главный список для хранения данных отчета — например,
    main_data — и поместить в него названия столбцов отчета в виде
    списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
    Значения для этих столбцов также оформить в виде списка и поместить в файл main_data
    (также для каждого файла);

    b) Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
    В этой функции реализовать получение данных через вызов функции get_data(),
    а также сохранение подготовленных данных в соответствующий CSV-файл;

    c) Проверить работу программы через вызов функции write_to_csv().
"""

import csv
from typing import Union
import re
import os.path

# список файлов с данными
data_files = ('info_1.txt', 'info_2.txt', 'info_3.txt')
path_to_csv = r'./test.csv'


def get_data(data: Union[str, list, tuple]):
    main_data = [['Изготовитель системы',
                 'Название ОС',
                  'Код продукта',
                  'Тип системы']]
    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []

    if isinstance(data, list) or isinstance(data, tuple):
        for file_name in data:
            with open(file_name, 'rb') as f_data:
                for row in f_data.read().decode('cp1251').splitlines():
                    os_prod = re.search(r'Изготовитель системы', row)
                    os_name = re.search(r'Название ОС', row)
                    os_code = re.search(r'Код продукта', row)
                    os_type = re.search(r'Тип системы', row)
                    data_row = row.split(':')
                    if os_prod:
                        os_prod_list.append(data_row[1].strip())
                    if os_name:
                        os_name_list.append(data_row[1].strip())
                    if os_code:
                        os_code_list.append(data_row[1].strip())
                    if os_type:
                        os_type_list.append(data_row[1].strip())

        for row in range(len(os_prod_list)):
            main_data.append([os_prod_list[row],
                              os_name_list[row],
                              os_code_list[row],
                              os_type_list[row]])

        return main_data


def write_to_csv(path_to_csv: str):
    if os.path.exists(path_to_csv):
        with open(path_to_csv, 'w+', encoding='utf-8') as file_csv:
            data_for_csv = get_data(data_files)
            csv_writer = csv.writer(file_csv)
            for row in data_for_csv:
                csv_writer.writerow(row)


write_to_csv(path_to_csv)

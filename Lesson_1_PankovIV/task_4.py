"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

words_set = ('разработка', 'администрирование', 'protocol', 'standard')
b_words_set = []

for byte_str in words_set:
    b_words_set.append(byte_str.encode('utf-8'))
print(f'{b_words_set}\n')

for string in b_words_set:
    print(string.decode('utf-8'))
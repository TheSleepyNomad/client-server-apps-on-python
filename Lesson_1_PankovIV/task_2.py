"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""
# Я не понял, можно ли изначально их так записать, поэтому вот два решения:
# 1)
byte_words_set = (b'class', b'function', b'method')
for word in byte_words_set:
    print(f'Слово - {word}. Тип {type(word)}')

# 2)
byte_words = []
for word in ('class', 'function', 'method'):
    byte_words.append(bytes(word, encoding='ascii'))

for word in byte_words:
    print(f'Слово - {word}. Тип {type(word)}')
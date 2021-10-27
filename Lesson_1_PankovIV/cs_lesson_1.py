import subprocess
import locale
# Задание №1
# Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате
# и проверить тип и содержание соответствующих переменных. Затем с помощью
# онлайн-конвертера преобразовать строковые представление в формат Unicode и
# также проверить тип и содержимое переменных

print('\nTask_1 ----->\n')
rus_words_set = ('разработка', 'сокет', 'декоратор')
for word in rus_words_set:
    print(f'Слово - {word}. Тип {type(word)}')

uni_wrods_set = ('\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
                 '\u0441\u043e\u043a\u0435\u0442',
                 '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440',)
for word in uni_wrods_set:
    print(f'Слово - {word}. Тип {type(word)}')


# Задание №2
# Каждое из слов «class», «function», «method» записать в байтовом типе без
# преобразования в последовательность кодов (не используя методы encode и decode)
# и определить тип, содержимое и длину соответствующих переменных.

print('\nTask_2 ----->\n')
byte_words_set = (b'class', b'function', b'method')
for word in byte_words_set:
    print(f'Слово - {word}. Тип {type(word)}')


# Задание №3
# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно
# записать в байтовом типе.

print('\nTask_3 ----->\n')
mix_words_set = ('attribute', 'класс', 'функция', 'type')
for word in mix_words_set:
    try:
        print(word.encode('ascii'))
    except UnicodeEncodeError:
        print(f'Слово {word} - невозможно записать в байтовом типе')


# Задание №4
# Преобразовать слова «разработка», «администрирование», «protocol», «standard»
# из строкового представления в байтовое и выполнить обратное преобразование
# (используя методы encode и decode).

print('\nTask_4 ----->\n')
words_to_byte = ('разработка', 'администрирование', 'protocol', 'standard')
b_words_set = []

for byte_str in words_to_byte:
    b_words_set.append(byte_str.encode('utf-8'))
print(f'{b_words_set}\n')

for string in b_words_set:
    print(string.decode('utf-8'))


# Задание №5
# Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из
# байтовового в строковый тип на кириллице.

print('\nTask_5 ----->\n')
ping_set = (subprocess.Popen(['ping', 'google.com'], stdout=subprocess.PIPE),
            subprocess.Popen(['ping', 'yandex.ru'], stdout=subprocess.PIPE),
            subprocess.Popen(['ping', 'youtube.com'], stdout=subprocess.PIPE),)


for subproc in ping_set:
    for line in subproc.stdout:
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))


# Задание №6
# Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование»,
# «сокет», «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в
# формате Unicode и вывести его содержимое.

print('\nTask_6 ----->\n')
local_encode = locale.getpreferredencoding()

with open('test_file.txt', 'w+') as file:
    file.writelines(('cетевое программирование',
                     'сокет',
                     'декоратор',))
    print(file)  # my default encode='cp1251'


try:
    # При принудительном открытии в Юникоде появляется ошибка
    with open('test_file.txt', 'r+', encoding='utf-8') as file:
        print(file.read())
except UnicodeDecodeError:
    print(
        f'Не получилось прочитать файл в кодировке utf-8. Открываем в {local_encode}')
    with open('test_file.txt', 'r+', encoding=local_encode) as file:
        print(file.read())

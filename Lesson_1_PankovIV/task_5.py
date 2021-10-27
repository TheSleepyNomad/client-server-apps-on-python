"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet

ping_set = (subprocess.Popen(['ping', 'google.com'], stdout=subprocess.PIPE),
            subprocess.Popen(['ping', 'yandex.ru'], stdout=subprocess.PIPE),
            subprocess.Popen(['ping', 'youtube.com'], stdout=subprocess.PIPE),)

for subproc in ping_set:
    for line in subproc.stdout:
        line = line.decode(chardet.detect(line).get('encoding')).encode('utf-8')
        print(line.decode('utf-8'))
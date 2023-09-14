# Создать программу, которая будет производить подсчет количества слов в каждом файле
# в указанной директории и выводить результаты в консоль.
# Используйте потоки.

import os
import threading
import time

directory = './Lesson_4/lesson4_task3'
threads = []
start_time = time.time()


def print_time(func):
    def wrapper(*args):
        start_time = time.time()
        func(*args)
        print(f'in {time.time() - start_time:.2f} sec')

    return wrapper


def file_listening(arg):
    f = os.path.join(directory, arg)
    words = 0
    if os.path.isfile(f):
        with open(f, encoding='utf-8') as file:
            for line in file:
                words += len(line.split())
        print(f'\nFile: {f:>53}  \twords: {words:>5} ')


@print_time
def loop_func():
    for _ in range(0, 10):
        for file_path in os.listdir(directory):
            thread = threading.Thread(target=file_listening, args=[file_path])
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()


loop_func()

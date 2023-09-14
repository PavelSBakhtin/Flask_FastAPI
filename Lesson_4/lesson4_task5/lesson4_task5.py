# Создать программу, которая будет производить подсчет количества слов в каждом файле
# в указанной директории и выводить результаты в консоль.
# Используйте процессы.

from multiprocessing import Process
import time
import os

directory = './Lesson_4/lesson4_task3'
processes = []
start_time = time.time()


def file_listening(arg):
    f = os.path.join(directory, arg)
    words = 0
    if os.path.isfile(f):
        with open(f, encoding='utf-8') as file:
            for line in file:
                words += len(line.split())
        print(f'\nFile: {f:>53}  \twords: {words:>5} in {time.time() - start_time:.2f} seconds')


if __name__ == '__main__':
    for file_path in os.listdir(directory):
        process = Process(target=file_listening, args=[file_path])
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

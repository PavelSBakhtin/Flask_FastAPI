# Создать программу, которая будет производить подсчет количества слов в каждом файле
# в указанной директории и выводить результаты в консоль.
# Используйте асинхронный подход.

import asyncio
import time
import os

directory = './Lesson_4/lesson4_task3'
tasks = []
start_time = time.time()


async def file_listening(arg):
    f = os.path.join(directory, arg)
    words = 0
    if os.path.isfile(f):
        with open(f, encoding='utf-8') as file:
            for line in file:
                words += len(line.split())
        print(f'\nFile: {f:>53}  \twords: {words:>5} in {time.time() - start_time:.6f} seconds')


async def main(arg):
    for file_path in os.listdir(arg):
        task = asyncio.ensure_future(file_listening(file_path))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main(directory))

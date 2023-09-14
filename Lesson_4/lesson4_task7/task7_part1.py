import random
import threading
import time

start_time = time.time()
threads = []

arr = [random.randint(0, 101) for _ in range(1, 1000001)]


def arr_sum(arg):
    res = sum(arg)
    print(f"{res} calculated in {time.time() - start_time:.2f} seconds")


for i in range(5):
    t = threading.Thread(target=arr_sum, args=[arr], daemon=True)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

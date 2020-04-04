import time


def timer():
    while True:
        limit_time = 10
        start = time.time()
        time.sleep(1)
        if time.time() - start >= limit_time:
            print('Время вышло(')
            return False
        else:
            print(int(limit_time - (time.time() - start)))
            return True

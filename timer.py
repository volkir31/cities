import time


def timer():
    start = time.time()
    while True:
        limit_time = 10
        time.sleep(1)
        if time.time() - start >= limit_time - 1:
            print('Время вышло(')
            valid_time = False
            break
        else:
            print(int(limit_time - (time.time() - start)))
            valid_time = True
    return valid_time


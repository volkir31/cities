import time


start = time.time()
for i in range(1, 900000000000000000000000000000000000000000):
    limit_time = 60
    time.sleep(1)
    if time.time() - start >= limit_time:
        print('Вы проиграли!\nПопробуйте еще раз')
        break
    else:
        print(f'У вас осталось { int(limit_time-(time.time() - start))}, поторопитесь!')
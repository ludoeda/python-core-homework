from ex2 import fetcher
import time

CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """
    def wrapper(func):
        # put your code here
        def innerWrapper(*args, **kwargs):
            totalTime = 0

            for n in range(num):
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                print(f'Время выполнения: {end - start}')
                totalTime += end - start

            print(f'Среднее время выполнения: {totalTime / num}')

        return innerWrapper

    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)



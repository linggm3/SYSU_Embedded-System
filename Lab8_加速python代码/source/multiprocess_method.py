import datetime
import math
from multiprocessing import Pool


def calculate(number):
    return math.sqrt(number) + number ** 2


def parallel_calculate(numbers):
    with Pool() as pool:
        results = pool.map(calculate, numbers)
    return results


def cal_sum_parallel(n):
    beforeCal = datetime.datetime.now()
    results = parallel_calculate(range(n))
    afterCal = datetime.datetime.now()
    calCost = afterCal - beforeCal
    return calCost


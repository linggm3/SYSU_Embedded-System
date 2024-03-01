import datetime
from numba import jit
import math

# 使用Numba的装饰器来编译这个函数
@jit
def calculate_sums(n):
    total_sum = 0
    for number in range(n):
        total_sum += math.sqrt(number) + math.pow(number, 2)
    return total_sum


def cal_sum_numba(n):
    beforeCal = datetime.datetime.now()
    # 计算总和
    result = calculate_sums(n)
    afterCal = datetime.datetime.now()
    calCost = afterCal - beforeCal
    return calCost


import datetime
import numpy as np


def cal_sum_numpy(n):
    beforeCal = datetime.datetime.now()
    numbers = np.arange(n)
    results = np.sqrt(numbers) + np.power(numbers, 2)
    afterCal = datetime.datetime.now()
    calCost = afterCal - beforeCal
    return calCost


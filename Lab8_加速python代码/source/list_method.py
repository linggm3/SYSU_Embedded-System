import datetime
import math


def cal_sum_list(n):
    before_cal = datetime.datetime.now()
    tmp = [math.sqrt(number) + number ** 2 for number in range(n)]
    after_cal = datetime.datetime.now()
    return after_cal - before_cal


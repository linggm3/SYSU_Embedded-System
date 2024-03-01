import datetime
import math


def cal_sum_navie(n):
    beforeCal = datetime.datetime.now()
    for number in range(n):
        result = math.sqrt(number ) + math.pow(number,2)
    afterCal=datetime.datetime.now()
    calCost = afterCal - beforeCal
    return calCost

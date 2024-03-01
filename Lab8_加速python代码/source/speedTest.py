from navie_method import cal_sum_navie
from numpy_method import cal_sum_numpy
from numba_method import cal_sum_numba
from list_method import cal_sum_list
from multiprocess_method import cal_sum_parallel
import datetime
import numpy as np
import platform
import cpuinfo


def measure_execution_time(function, n):
    before_cal = datetime.datetime.now()
    _ = function(n)
    after_cal = datetime.datetime.now()
    return (after_cal - before_cal).total_seconds()


def get_system_info():
    cpu_details = cpuinfo.get_cpu_info()
    info = {
        "操作系统": platform.system(),
        "系统版本": platform.version(),
        "主机名称": platform.node(),
        "机器类型": platform.machine(),
        "CPU类型": platform.processor(),
        "CPU品牌": cpu_details['brand_raw'],
        "核心数量": cpu_details['count'],
        "核心速度": cpu_details['hz_actual_friendly']
    }
    return info


if __name__ == '__main__':
    # 定义不同的输入规模
    input_scales = [1000, 10000, 100000, 1000000, 10000000, 100000000]

    # 定义不同的方法
    methods = [cal_sum_navie, cal_sum_numpy, cal_sum_numba, cal_sum_list, cal_sum_parallel]

    # 创建5x5矩阵来存储结果
    results = np.zeros((6, 5))

    # 测试每种方法在每种输入规模下的运行时间
    for i, n in enumerate(input_scales):
        for j, method in enumerate(methods):
            results[i, j] = measure_execution_time(method, n)

    system_info = get_system_info()
    for key, value in system_info.items():
        print(f"{key}: {value}")
    print()
    print("运行时间矩阵 (行：规模, 列：方法):")
    print("输入规模：", input_scales)
    for row in results:
        # 对每一行进行格式化，使每个值显示为6位小数
        print(" ".join(f"{item:.6f}" for item in row))



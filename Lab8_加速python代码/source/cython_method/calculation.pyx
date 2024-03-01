# calculation.pyx
from libc.math cimport sqrt, pow

def calculate_sums(int n):
    cdef int number
    cdef double total_sum = 0
    for number in range(n):
        total_sum += sqrt(number) + pow(number, 2)
    return total_sum

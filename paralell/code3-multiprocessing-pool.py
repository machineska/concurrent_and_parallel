import math
import numpy as np
from timebudget import timebudget
from multiprocessing import Pool


iterations_count = round(1e7)
def complex_operation(input_index):
   print("Complex operation. Input index: {:2d}".format(input_index))
   [math.exp(i) * math.sinh(i) for i in [1] * iterations_count]

def complex_operation_numpy(input_index):
      print("Complex operation (numpy). Input index: {:2d}".format(input_index))
      data = np.ones(iterations_count)
      np.exp(data) * np.sinh(data)


@timebudget
def run_complex_operations(operation, input, pool):
    return pool.map(operation, input)

processes_count = 10

input = range(10)

if __name__ == '__main__':
    processes_pool = Pool(processes_count)
    print('native math')
    data_nat = run_complex_operations(complex_operation, input, processes_pool)
    print()
    print('numpy..')
    data_np = run_complex_operations(
            complex_operation_numpy, input, processes_pool
    )



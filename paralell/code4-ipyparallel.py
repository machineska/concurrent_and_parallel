import math
import numpy as np
from timebudget import timebudget
import ipyparallel as ipp

# run onm terminal to start cluster
# ipcluster start -n 10

iterations_count = round(1e7)

def complex_operation(input_index):
    print("Complex operation. Input index: {:2d}".format(input_index))
    import math
    [math.exp(i) * math.sinh(i) for i in [1] * round(1e7)]

def complex_operation_numpy(input_index):
    print("Complex operation (numpy). Input index: {:2d}".format(input_index))
    
    import numpy as np

    data = np.ones(round(1e7))
    np.exp(data) * np.sinh(data)

@timebudget
def run_complex_operations(operation, input, pool):
    return pool.map(operation, input)

client_ids = ipp.Client()
pool = client_ids[:]

input = range(10)
print('Without NumPy')
data_numpy = run_complex_operations(complex_operation, input, pool)
print(data_numpy.get())
print('NumPy')
data_ipp = run_complex_operations(complex_operation_numpy, input, pool)
print(data_ipp.get())

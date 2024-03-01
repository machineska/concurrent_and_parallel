import math
import time

iterations_count = round(1e7)
def complex_operation(input_index):
   print("Complex operation. Input index: {:2d}".format(input_index))
   [math.exp(i) * math.sinh(i) for i in [1] * iterations_count]

input = range(10)

start = time.time()
data = list(map(complex_operation, input) )
end = time.time()
print(f'execution took {end - start} seconds')
print(data)

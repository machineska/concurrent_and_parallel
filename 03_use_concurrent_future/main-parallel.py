import collections
import time
import concurrent.futures
import os
import random
from pprint import pprint

random.seed(200)

Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel',
])

scientists = (
    Scientist(name='Ada Lovelance', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
    Scientist(name='Tu Youyou', field='chemistry', born=1938, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
    Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', born=1951, nobel=False),
)

pprint(scientists)
print()

def transform(x):
    print(f'Processing {os.getpid()} record {x.name}')
    delay = 1 # random.randint(1, 5)
    time.sleep(delay)
    print(f'Delay with {delay} seconds..')
    result = {'name': x.name, 'age': 2023 - x.born}
    print(f'Done processing {os.getpid()} record {x.name}')
    print()
    return result

if __name__ == '__main__':
    start = time.time()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        result = executor.map(transform, scientists)

    #result = tuple(map(
    #    transform,
    #    scientists
    #))

    end = time.time()

    print(f'Time to completion {end - start} seconds')

    pprint(tuple(result))

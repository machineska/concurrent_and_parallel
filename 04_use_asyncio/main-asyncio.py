import asyncio
import collections
import os
import time
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



async def transform(x):
    print(f'Processing {os.getpid()} record {x.name}')
    delay = 1 # random.randint(1, 5)
    await asyncio.sleep(delay)
    print(f'Delay with {delay} seconds..')
    result = {'name': x.name, 'age': 2023 - x.born}
    print(f'Done processing {os.getpid()} record {x.name}')
    print()
    return result

async def get_result():
	r = await asyncio.gather(*(transform(x) for x in scientists))
	return r

if __name__ == "__main__":
    start = time.time()
    result = asyncio.run(get_result())
    end = time.time()
    print(f'Time to completion {end - start} seconds')
    pprint(result)

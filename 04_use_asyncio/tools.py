import asyncio
from functools import wraps, partial


def to_async(func):
    @wraps(func)  # Makes sure that function is returned for e.g. func.__name__ etc.
    async def run(loop=None, executor=None,):
        if loop is None:
            loop = asyncio.get_event_loop() # Make event loop of nothing exists
        pfunc = partial(func)  # Return function with variables (event) filled in
        return await loop.run_in_executor(executor, pfunc)
    return run

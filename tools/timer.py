import math
import time
from contextlib2 import contextmanager


@contextmanager
def cal_time(name=""):
    start = time.time()
    yield
    print(f"{name} done in {math.ceil(time.time() - start)} s", )

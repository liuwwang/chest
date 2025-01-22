import time
from rich.console import Console
from contextlib2 import contextmanager

console = Console()


@contextmanager
def cal_time(name=""):
    start = time.time()
    yield
    console.log(f"{name} done in {round(time.time() - start, 4)} s", )

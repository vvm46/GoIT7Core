# from my_package.foo import foo
# from my_package.baz.operation import sum, mul
# from my_package.bar.info import log

from .foo import foo
from .baz.operation import sum, mul
from .bar.info import log, foo as temp

__all__ = ["foo", "sum", "mul", "log", "temp"]


print("My custom package")
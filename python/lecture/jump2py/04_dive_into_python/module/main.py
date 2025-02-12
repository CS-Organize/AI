# Other modules in the same directory

# import <module> [as <alias>]
# from <module> import <name> [as <alias>]
import aec
print(aec.FG_RED + 'Hello, world!' + aec.RESET)

import aec as a
print(a.FG_YELLOW + 'Hello, world!' + a.RESET)

from aec import FG_GREEN, RESET

print(FG_GREEN + 'Hello, world!' + RESET)

from aec import FG_BLUE as blue, RESET as reset

print(blue + 'Hello, world!' + reset)

from aec import *

print(FG_MAGENTA + 'Hello, world!' + RESET)

# __name__, __main__
print("ace.__name__ is " + aec.__name__)

# Other modules in the other directory

# sys.path
import sys

for path in sys.path:
    print(path)
sys.path.append('/Users/anseungwon/dev/Python/python/jump2py/03_io')
for path in sys.path:
    print(path)

import py_io

py_io.print_color(py_io.FG_RED, "Function")

# Export PYTHONPATH="path"

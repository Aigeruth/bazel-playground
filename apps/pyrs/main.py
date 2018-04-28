from ctypes import cdll
import os
from re import match


def load_library(pattern):
    for root, dirs, files in os.walk('.'):
        for name in files:
            if match(pattern, name):
                return cdll.LoadLibrary(os.path.join(root, name))


math = load_library(r'libmath.*\.(so|dylib)')
print("Square of 16 is {:d}.".format(math.square(16)))

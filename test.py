import sys
import os

print('Hello World!')

for arg in sys.argv:
    print(arg)

print(os.environ.get('INPUT_TEST'))
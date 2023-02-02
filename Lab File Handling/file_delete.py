import os
try:
    os.remove('my_firs_file.txt')
except FileNotFoundError:
    print('File already deleted!')
# sub_dir_search2.py

import os

try:
    for (path, dir, files) in os.walk("C:/"):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.py':
                print("%s/%s" % (path, filename))
except PermissionError:
    pass

# tab_to_space.py
# Replace tabs with 4 spaces

import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " " * 4)
print(space_content)

# print(src)
# print(dst)

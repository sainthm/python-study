# memo.py

# >python memo.py -a "Life is too short"

import sys

option = sys.argv[1]
# memo = sys.argv[2]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()

# print(option)
# print(memo)
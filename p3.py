#! python

import math

from file_in import load

def process_input(i):
    t = [l.rstrip() for l in load(i)]
    return t

if __name__ == '__main__':
    i = process_input('i3')
    tree_counts = []
    for slope in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
        x = 0
        count = 0
        for y in range(0,len(i),slope[1]):
            c=i[y]
            if i[y][x] == '#':
                count+=1
            x = (x+slope[0])%31
        tree_counts.append(count)
    print(math.prod(tree_counts))
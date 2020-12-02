#! python

from file_in import load

def process_input(l):
    o=[]
    l = load(l)
    for n in l:
        o.append(int(n))
    return o

if __name__ == "__main__":
    i = process_input('i1')

    for v in range(len(i)):
        for m in range(v, len(i)-v):
            for o in range(m, len(i)-m):
                if i[v] + i[m] + i[o] == 2020:
                    print(i[v]*i[m]*i[o])
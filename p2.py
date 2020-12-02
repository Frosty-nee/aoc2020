#! python

from file_in import load

def process_input(lf):
    out = []
    l = load(lf)
    for k in l:
        interm = k.split(': ')
        interm[1] = interm[1].rstrip()
        out.append((interm[0],interm[1]))
    return(out)

def policy(s):
    r,c = s[0].split(' ')
    mn,ma = [int(i) for i in r.split('-')]
    return (mn, ma, c)

if __name__ == '__main__':
    i = process_input('i2')
    valid_passwords = 0
    for v in i:
        i,j,c = policy(v)
        i-=1
        j-=1
        v = v[1]
        l = len(v)
        if (v[i] == c and v[j] != c) or (v[i] != c and v[j] == c):
            valid_passwords+=1
    print(valid_passwords)


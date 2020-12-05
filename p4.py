#! python

import string

from file_in import load

def process_input(i):
    i = load(i)
    p = ''
    for line in i:
        if line != '\n':
            p+=line.strip()+' '
        else:
            p= p.rstrip() + '\n'
    p=p.rstrip()
    p = p.split('\n')

    passports = []
    for passport in p:
        d = {}
        split = passport.split(' ')
        for item in split:
            k,v = item.split(':')
            d[k] = v
        passports.append(d)
    return passports

def validate(k, v):
    if k == 'byr':
        i = int(v)
        return(i >= 1920 and i <= 2002)
    elif k == 'iyr':
        i = int(v)
        return(i >= 2010 and i <= 2020)
    elif k == 'eyr':
        i = int(v)
        return(i >=2020 and i<= 2030)
    elif k == 'hgt':
        if len(v) <4:
            return False
        unit = v[-2:]
        value = int(v[:len(v)-2])
        if unit == 'cm':
            return value >= 150 and value <= 193
        elif unit == 'in':
            return value >= 59 and value <= 76
        else:
            return False
    elif k == 'hcl':
        allowed_chars = string.hexdigits
        valid = True
        if v[0] == '#' and v[1:].isalnum() and len(v) == 7:
            for c in v[1:]:
                if c not in allowed_chars:
                    valid = False
                    break
        else:
            valid = False
        return valid
    elif k == 'ecl':
        allowed_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        return v in allowed_colors
    elif k == 'pid':
        return len(v) == 9 and v.isnumeric()
    elif k == 'cid':
        return True
    else:
        return False

if __name__ == '__main__':
    passports = process_input('i4')
    count = 0
    for passport in passports:
        valid = True
        if len(passport.keys()) == 8 or (len(passport.keys()) == 7 and 'cid' not in list(passport.keys())):
            for k,v in passport.items():
                if not validate(k,v):
                    valid = False
                    break
        else:
            valid = False
        if valid:
            count +=1
    print(count)
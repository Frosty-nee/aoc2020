#! python

import math

from file_in import load

def process_input(i):
    i.sort()
    return [(find_row_or_column(e[:7]), find_row_or_column(e.strip()[7:])) for e in reversed(i)]

def find_row_or_column(i):
    r = range(2**len(i))
    i = [True if b == 'F' or b == 'L' else False for b in i]
    for c in i:
        if c:
            r = r[:int(len(r)/2)]
        else:
            r = r[int(len(r)/2):]
    return r[0]

def calc_seat_id(seat):
    return 8 * seat[0] + seat[1]

def check_if_neighbors_exist(i, seats):
    if seats[i+1] != seats[i]+1 and seats[i+2] != seats[i]+2:
        return seats[i]+1
    else:
        return None

if __name__ == '__main__':
    seats = process_input(load('i5'))
    seat_ids = [calc_seat_id(s) for s in seats]
    seat_ids.sort()
    for s, v in enumerate(seat_ids):
        if check_if_neighbors_exist(s, seat_ids):
            print(v+1)
            break
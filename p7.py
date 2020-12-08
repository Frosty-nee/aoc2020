#! python

import math

from file_in import load

def process_input(i):
    i=[r.strip() for r in i]
    d = {}
    for rule in i:
        color, contains = rule.split(' contain ')
        color = trim(color, 's')
        rdict = {}
        for e in contains.split(', '):
            e = trim(e, '.')
            e = trim(e, 's')
            result = e.split(' ', 1)
            rdict[result[1]] = result[0]
        d[color] = rdict
    return d

def trim(s, c):
    if s[-1] == c:
        s = s[:-1]
    return(s)


def p1_count():
    def get_contained_bags_p1(rule):
        if rule_list[rule] == {'other bag': 'no'}:
            return set()
        contained_bags = set()
        for bag in rule_list[rule]:
            contained_bags.add(bag)
        inter = set()
        for bag in contained_bags:
            inter.update(get_contained_bags_p1(bag))
        contained_bags.update(inter)
        return contained_bags
    count = 0
    for rule in rule_list:
        if 'shiny gold bag' in get_contained_bags_p1(rule):
            count += 1
    return count

def get_contained_bags(bag):
    if rule_list[bag] == {'other bag': 'no'}:
        return {}
    else:
        d = rule_list[bag]
        for e in d:
            d[e] = int(d[e])
    return d

def merge_dicts(d1, d2):
    for k,v in d2.items():
        if k in d1:
            d1[k] = d1[k] + int(v)
        else:
            d1[k] = int(v)
    return d1

def count_contained_bags(i):
    if get_contained_bags(i) == {}:
        return 1
    else:
        bagcount = 1
        for bag, number in get_contained_bags(i).items():
            bagcount += (number * count_contained_bags(bag))
    return bagcount

if __name__ == '__main__':
    global rule_list
    rule_list = process_input(load('i7'))

    print(p1_count())
    print(count_contained_bags('shiny gold bag')-1)
#! python
import p7

testinput = {
    'pale green bag': {'dark purple bag': 2, 'bright green bag': 1},
    'dark purple bag': {'dark yellow bag': 6, 'bright orange bag': 3},
    'bright green bag': {},
    'bright orange bag':{'bright green bag':1},
    'dark yellow bag':{},
    }

p7.rule_list = testinput
print(p7.count_contained_bags('dark purple bag'))
assert p7.count_contained_bags('dark purple bag')-1 == 12
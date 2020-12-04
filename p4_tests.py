#! python

from p4 import validate

if __name__ == '__main__':
    assert validate('byr', '1919') == False
    assert validate('byr', '1920') == True
    assert validate('byr', '2002') == True
    assert validate('byr', '2003') == False

    assert validate('iyr', '2009') == False
    assert validate('iyr', '2010') == True
    assert validate('iyr', '2020') == True
    assert validate('iyr', '2021') == False

    assert validate('eyr', '2019') == False
    assert validate('eyr', '2020') == True
    assert validate('eyr', '2030') == True
    assert validate('eyr', '2031') == False

    assert validate('hgt', '149cm') == False
    assert validate('hgt', '150cm') == True
    assert validate('hgt', '150') == False
    assert validate('hgt', 'cm') == False
    assert validate('hgt', '60i') == False
    assert validate('hgt', '58in') == False
    assert validate('hgt', '59in') == True
    assert validate('hgt', '76in') == True
    assert validate('hgt', '77in') == False

    assert validate('hcl', 'abc123') == False
    assert validate('hcl', '#abc123') == True
    assert validate('hcl', '#abg123') == False
    assert validate('hcl', '#1234567') == False
    assert validate('hcl', '#1234') == False

    assert validate('pid', '12345') == False
    assert validate('pid', '123457689') == True
    assert validate('pid', 'ab3456789') == False
    assert validate('pid', '1234567800123') == False
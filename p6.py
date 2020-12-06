#! python

import string

from p4 import preprocess
from file_in import load

if __name__ == '__main__':
    groups = preprocess(load('i6'))
    count =0
    for group in groups:
        questions = set(string.ascii_lowercase)
        for individual in group.split(' '):
            for response in string.ascii_lowercase:
                if response not in individual:
                    try:
                        questions.remove(response)
                    except:
                        pass
        count += len(questions)
    print(count)
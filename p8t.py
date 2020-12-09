#! python

from p8 import run_instructions, test_changing_jmp

if __name__ == '__main__':
    test_instructions = ['acc +12', 'jmp +2', 'acc +3', 'jmp -1', 'acc +10', 'nop +3']

    #print(run_instructions(test_instructions))
    test_changing_jmp(test_instructions)
#! python

from file_in import load

def process_input(i):
    return [line.strip() for line in i]

def run_instructions(instruction_list):
    def handle_instruction(index):
        instruction = instruction_list[index].split(' ')
        instruction[1] = int(instruction[1])
        return handlers[instruction[0]](instruction[1])
    def handle_nop(mod):
        if handle_jmp(mod)[2] > 600:
            pass
        return current_index, 0, current_index+1
    def handle_acc(mod):
        return current_index, mod, current_index+1
    def handle_jmp(mod):
        if current_index+1 > 630:
            pass
        return current_index, 0, current_index+mod
    handlers = {
        'acc': handle_acc,
        'nop': handle_nop,
        'jmp': handle_jmp,
    }
    processed_instructions = set()
    accumulator = 0
    current_index = 0
    while True:
        if current_index >= len(instruction_list):
            return accumulator
        current, modifier, nxt = handle_instruction(current_index)
        accumulator += modifier
        processed_instructions.add(current)
        current_index = nxt
        if current_index in processed_instructions:
            #print(accumulator, current_index, max(processed_instructions))
            return None
        if current_index > len(instruction_list):
            break
    return accumulator, current_index

def test_changing_nop(instruction_list):
    for index, entry in enumerate(instruction_list):
        if entry.split(' ')[0] == 'nop':
            backup_instructions = instruction_list
            instruction_list[index] = ' '.join(('jmp', entry.split(' ')[1]))
            if run_instructions(instruction_list) != None:
                print(index, run_instructions(instruction_list))
            instruction_list = backup_instructions

def test_changing_jmp(instruction_list):
    backup_instructions = instruction_list.copy()
    for index, entry in enumerate(instruction_list):
        if entry.split(' ')[0] == 'jmp':
            instruction_list = backup_instructions.copy()
            instruction_list[index] = ' '.join(('nop', entry.split(' ')[1]))
            if run_instructions(instruction_list) != None:
                print(index, run_instructions(instruction_list))

if __name__ == '__main__':
    instruction_list = process_input(load('i8'))
    #print(run_instructions(instruction_list))
    #test_changing_nop(instruction_list)
    test_changing_jmp(instruction_list)

'''A robot arm is programmed to do very basic instructions
P for Pick block, M for Move block, and L for lower a block.
The arm is forgetful and works with certain constraints.
The arm always picks blocks from an infinite stash.
There are 10 horizontal positions and 16 vertical positions to count
blocks places by the arm (m by n matrix).
The compute method accepts a series of sequences (P, M and L only - other
instructions are ignored). There are couple of rules by which the arm operates.
The objective is to return the block positions - that is, count of blocks generated
after the sequence executes in hexadecimal form
'''
def  compute(instructions):
    '''Returns block state after the Robot carries out
        instructions.
        \rinstructions: string sequence of instructions'''
    hex_code = [str(i) for i in range(10)]
    [hex_code.append(chr(i)) for i in range(65, 71)]
    max_positions = 9
    blocks = ['0'] * max_positions
    current_pos = 0
    current_block = 1
    isheld = False
    if instructions is None:
        return None
    for i in instructions:
        if i == 'P':
            if isheld:
                current_pos = 0
            isheld = True
        elif i == 'M':
            current_pos += 1
            current_pos = current_pos % max_positions
        elif i == 'L':
            tmp = blocks[current_pos]
            tmp = hex_code.index(str(blocks[current_pos]))
            if tmp:
                # tmp = int(tmp, 0)
                current_block += tmp
            hex_block = hex_code[current_block]
            if hex_block == 'F':
                isheld = True
            else:
                isheld = False
            blocks[current_pos] = hex_block
            current_pos = 0 #reset current position counter
            current_block = 1 #reset current block counter
    print(''.join([str(s) for s in blocks]))

compute('PMLPMMMLPMLPMML') #returns 021100000
compute('PLPLPLPLPLPLPLPLPLPL') #returns A00000000

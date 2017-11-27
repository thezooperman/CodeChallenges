def convertToHexa(n):
    '''Convert to Hexadecimal from decimal.
        \rn: decimal value
    '''
    if n < 0:
        return 0
    elif n <= 1:
        return n
    else:
        convertToHexa(n // 16)
        x = n % 16
        if x < 10:
            return x
        if x == 10:
            return 'A'
        if x == 11:
            return 'B'
        if x == 12:
            return 'C'
        if x == 13:
            return 'D'
        if x == 14:
            return 'E'
        if x == 15:
            return 'F'

def  compute(instructions):
    '''Returns block state after the Robot carries out
        instructions.
        \rinstructions: string sequence of instructions'''
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
            if tmp:
                tmp = int(str(tmp), 0)
                current_block += tmp
            hex_block = convertToHexa(current_block)
            if hex_block == 'F':
                isheld = True
            else:
                isheld = False
            blocks[current_pos] = hex_block
            current_pos = 0 #reset current position counter
            current_block = 1 #reset current block counter
    print(''.join([str(s) for s in blocks]))

compute('PMLPMMMLPMLPMML') #returns 0211000000
compute('') #returns 000000000

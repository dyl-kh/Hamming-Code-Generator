from distutils.log import error
import getValidInput
import parityGroups


def decode():
    print('-' * 50)
    print()
    print('You are now in the decoder')
    print('Type MENU at anytime to return to the menu')
    print()

    # get user input from command line limited 11 bits
    user_input = getValidInput.get(11)
    if user_input == 'MENU':  # return to menu if user enters MENU
        return

    # get parity bit groups
    parity_groups = parityGroups.get()
    # list of indexes of bits that are in error
    error_bit_indexes = list(range(0, 11))
    # list of indexes of bits in the hamming code
    index_list = list(range(0, 11))

    error = False

    # check parity bits
    for i in parity_groups:  # loop through each parity group
        parity = 0
        for j in parity_groups[i]:  # loop through each bit in the parity group
            if user_input[j] == '1':  # check if bit is 1
                parity += 1
        if parity % 2 != 0:  # check if parity is odd
            error = True
            toRemove = list(set(index_list) - set(parity_groups[i]))
            for k in toRemove:  # remove each bit not in the parity group
                try:
                    if k != i:
                        error_bit_indexes.remove(k)
                except Exception:
                    pass
        else:
            for j in parity_groups[i]:  # remove each bit in the parity group
                try:
                    error_bit_indexes.remove(j)
                except Exception:
                    pass

    if error:
        print('Bit Error Detected')
        error_bit = error_bit_indexes[0]
        print('At index:', error_bit)
        print('Flipping bit...')
        if user_input[error_bit] == '1':
            user_input[error_bit] = '0'
        else:
            user_input[error_bit] = '1'

        code_str = ''.join(str(i) for i in user_input)
        print('Corrected Hamming Code:', ''.join(code_str))
    else:
        print('There is no error in the input bits')

    # remove parity bits
    user_input.pop(0)
    user_input.pop(0)
    user_input.pop(1)
    user_input.pop(4)

    user_input.reverse()
    code_str = ''.join(str(i) for i in user_input)
    print('Decoded Bits:', code_str)

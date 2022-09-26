import getValidInput
import parityGroups


def encode():
    # get user input from command line limited 7 bits

    print('-' * 50)
    print()
    print('You are now in the encoder')
    print('Type MENU at anytime to return to the menu')
    print()

    user_input = getValidInput.get(7)
    if user_input == 'MENU':
        return

    # set parity bit groups
    parity_groups = parityGroups.get()

    # initialize hamming code list
    hamming_code = [-1, -1, user_input[0], -1, user_input[1], user_input[2],
                    user_input[3], -1, user_input[4], user_input[5], user_input[6]]

    # calculate parity bits
    for i in parity_groups:
        parity = 0
        for j in parity_groups[i]:
            if hamming_code[j] == '1':
                parity += 1
        if parity % 2 == 0:
            hamming_code[i] = '0'
        else:
            hamming_code[i] = '1'

    hamming_code.reverse()
    hamming_code_str = ''.join(str(i) for i in hamming_code)

    print('Hamming code:', hamming_code_str)

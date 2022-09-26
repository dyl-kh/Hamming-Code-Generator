import readline


def get(length):
    # get user input from command line limited 7 bits
    valid = False
    while valid == False:

        print(f'Input {length} bits of binary data: ',
              end='')  # prompt user for input
        user_input = input()  # get user input
        print()

        if user_input == 'MENU':
            return user_input

        user_input = list(user_input)  # split user input into list
        user_input.reverse()  # reverse list
        if len(user_input) != length:  # check if user input is 7 bits

            print('**ERROR**')
            print(f'Input must be {length} bits')
            print('Please try again')
            print()
            continue

        # validate user input
        for i in user_input:
            if i == '0' or i == '1':
                valid = True
            else:
                valid = False
                print('**ERROR**')
                print('Input must only contain 1s and 0s')
                print('Please try again')
                print()
                break

    return user_input

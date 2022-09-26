import decoder
import encoder

run = True
print('-' * 50)
print('Welcome to Hamming Code Encoder/Decoder')
print()

while run:  # main loop
    print('--Menu--')
    print('1. Encode')
    print('2. Decode')
    print('3. Exit')
    print()
    user_choice = input('Enter a selection: ')
    print()
    if user_choice == '1':  # encode
        encoder.encode()
        print()
    elif user_choice == '2':  # decode
        decoder.decode()
        print()
    elif user_choice == '3':  # exit
        print('Exiting...')
        print('Goodbye :)')
        run = False
    else:  # invalid input
        print('**ERROR**')
        print('Invalid selection')
        print('Please try again')
        print()

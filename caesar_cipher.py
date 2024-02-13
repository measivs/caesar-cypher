from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 
'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
'u', 'v', 'w', 'x', 'y', 'z']

def caesar(t, sh, d):
    new_text = ''
    if d == 'decode':
        sh *= -1
    for i in t:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = position + sh
            new_letter = alphabet[new_position]
            new_text += new_letter  
        else:
            new_text += i  
    print(f'the {d}d text is {new_text}')

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(text, shift, direction)
    restart = input('do you want to restart the cipher program? (yes/no)\n')
    if restart == 'no':  
        should_continue = False
        print('okay, goodbye!')









# while True:
#     restart = input('do you want to restart the cipher program? (yes/no)\n')
#     if restart == 'yes':
#         direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#         text = input("Type your message:\n").lower()
#         shift = int(input("Type the shift number:\n"))
#         caesar(text, shift, direction)
#     else:
#         print('okay, goodbye!')
#         break



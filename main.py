# Ethan Lawrence
# Oct 8 2024
# Cipher

# Incription
alphabet = 'abcdefghijklmnopqrstuvwxyx'
new_message = ''

user_message = input('Enter your super secret message:  ').lower()
key = int(input('Enter a key:   '))
# print(user_message)

for charcter in user_message:
    if charcter in alphabet:
        position = alphabet.find(charcter)
        new_position = (position + key) % 26
        new_character = alphabet[new_position]
        new_message += new_character
    
    else:
        new_message += charcter

print('Your new message is: ' + new_message)


'''
# Decription
alphabet = 'abcdefghijklmnopqrstuvwxyx'
new_message = ''

user_message = input('Enter your super secret INCRIPTED message:  ').lower()
key = int(input('Enter a key:   '))
# print(user_message)

for charcter in user_message:
    if charcter in alphabet:
        position = alphabet.find(charcter)
        new_position = (position - key) % 26
        new_character = alphabet[new_position]
        new_message += new_character
    
    else:
        new_message += charcter

print('Your new message is: ' + new_message)
'''
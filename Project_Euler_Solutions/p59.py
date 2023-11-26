'''
Each character on a computer is assigned a unique code and the preferred standard is ASCII 
(American Standard Code for Information Interchange). For example, uppercase A = 65, 
asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, 
then XOR each byte with a given value, taken from a secret key. 
The advantage with the XOR function is that using the same encryption key on the cipher text, 
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, 
and the key is made up of random bytes. The user would keep the encrypted message 
and the encryption key in different locations, and without both "halves", 
it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method 
is to use a password as a key. If the password is shorter than the message, which is likely, 
the key is repeated cyclically throughout the message. The balance for this method 
is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. 
Using 0059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, 
and the knowledge that the plain text must contain common English words, 
decrypt the message and find the sum of the ASCII values in the original text.
'''

import string

def string_to_ascii(s):
    """Convert a string to a list of ASCII values."""
    return [ord(c) for c in s]

def ascii_to_string(ascii_list):
    """Convert a list of ASCII values back to a string."""
    return ''.join(chr(code) for code in ascii_list)

#Decodes message with three letter key and returns sum of ascii characters
def decode_three_letter_key(code):
    solved=False
    sum=0

    # Iterate over each letter in the alphabet
    for first_letter in string.ascii_lowercase:
        if solved:
            break
        for second_letter in string.ascii_lowercase:
            if solved:
                break
            for third_letter in string.ascii_lowercase:
                # Combine the letters 
                letters=string_to_ascii(first_letter + second_letter + third_letter)

                #Extend the list lst to length n by repeating its elements.
                key=[letters[i % len(letters)] for i in range(len(code))]

                message=[code[i]^key[i] for i in range(len(code))]
                decripted=ascii_to_string(message)
                
                if 'Euler' in decripted:
                    print(first_letter + second_letter + third_letter)
                    print(decripted)
                    solved=True
                    for l in message:
                        sum+=l
                    break

    return sum

#Name of file with encrypted message
name='0059_cipher.txt'

#Opens file
file= open(name, 'r')

#characters
codes=[]
for line in file:
    row=line.split(',')
    for n in row:
        codes.append(int(n))

print(decode_three_letter_key(codes))

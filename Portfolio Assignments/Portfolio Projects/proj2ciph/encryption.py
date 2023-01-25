# encryption.py
# Marcos Perez, ENDG 233 F21
# A terminal-based encryption application capable of both encoding and decoding text when given a specific cipher.
# You may optionally import the string module from the standard Python library. No other modules may be imported.
# Remember to include docstrings for your functions and comments throughout your code.
import string



### Define your functions here
def encode(text, cipher): # Function for encoding, takes in a text and cipher string and outputs an encoded string

    alpha = list(string.ascii_lowercase) # Creating alphabet list
    alpha_cipher_pair = dict(zip(alpha,cipher)) # Creating dict with the list and the string

    translated_text = [] # Translates text by using the cipher dictionary to replace values in the input text
    for x in text:
        translated_text.append(alpha_cipher_pair[x])
    
    return "".join(translated_text)

def decode(text, cipher): # Function for decoding, takes in a text and cipher string and outputs a decoded string

    alpha = list(string.ascii_lowercase) # Creating alphabet list
    alpha_cipher_pair = dict(zip(alpha,cipher)) # Creating dict with the list and the string
    cipher_alpha_pair = {y:x for x,y in alpha_cipher_pair.items()} # Flips dict in order to decode instead of encode

    translated_text = [] # Translates text by using the cipher dictionary to replace values in the input text
    for x in text:
        translated_text.append(cipher_alpha_pair[x])
    
    return "".join(translated_text)

def validate(cipher): # Function that validates a cipher string, outputs True or False
    
    if(len(cipher) > 26 or len(cipher) < 26 or cipher.isalnum() == False):
        return False

    return True

def removedupli(cipher): # Function that removes duplicates from a cipher string
    cipher = "".join(dict.fromkeys(cipher))
    
    return cipher


    



print("ENDG 233 Encryption Program")

### Add your main program code here
menu = {} # Menu options
menu['0']="End program." 
menu['1']="Encode text"
menu['2']="Decode text"

while True: # Main loop for menu
    options=menu.keys() 
    
    print("\nENDG 233 Encryption Program\n")

    for entry in options: # Mrinting options for menu
        print(entry, menu[entry])

    selection = input('\nPlease Select: ') 

    if selection == '1': # Main logic switch - encodes text

        text = input('Please enter the text to be processed: ') # Inputs for text and cipher
        cipher = input('Please enter the cipher text: ')

        cipher_lowercase = cipher.lower() # This block validates/processes the cipher, and if determined to be valid, uses the cipher to encode text.
        if (validate(cipher_lowercase) == False):

            if (validate(removedupli(cipher_lowercase))) == True:

                cipher_lowercase = removedupli(cipher_lowercase)
                print('your cipher is valid')
                print(encode(text, cipher_lowercase))
            else:

                print('Your cipher must be made of 26 unique alpha-numeric characters')
        else:
            
            print('your cipher is valid')
            print(encode(text, cipher_lowercase))

    elif selection == '2': # Main logic switch - decodes text

        text = input('Please enter the text to be processed: ') # Inputs for text and cipher
        cipher = input('Please enter the cipher text: ')

        cipher_lowercase = cipher.lower() # This block validates/processes the cipher, and if determined to be valid, uses the cipher to decode text.
        if (validate(cipher_lowercase) == False):

            if (validate(removedupli(cipher_lowercase))) == True: 

                cipher_lowercase = removedupli(cipher_lowercase)
                print('your cipher is valid')
                print(decode(text, cipher_lowercase))

            else:

                print('Your cipher must be made of 26 unique alpha-numeric characters')
        else:

            print('your cipher is valid')
            print(decode(text, cipher_lowercase))

    elif selection == '0': # main logic switch - ends program

        break
    else: # Case for unkown menu input

        print('Unknown Option Selected!')  


print('Thank you for using the encryption program.')


import string

def translateCUS(pair, text):
    translated_text = []
    for x in text:
        translated_text.append(pair[x])
    
    return "".join(translated_text)

def detranslateCUS(pair, text):
    pair = {y:x for x,y in pair.items()}

    translated_text = []
    for x in text:
        translated_text.append(pair[x])
    
    return "".join(translated_text)







testc = 'c5zf0hijklgn4bqrmtdvwx6za3'
test = 'jumpedoverthelazy'


alpha = list(string.ascii_lowercase) # Creating alphabet list
# for i, item in enumerate(alpha): # Converting characters in alphabet list to unicode
#    alpha[i] = ord(alpha[i])

alpha_cipher_pair = dict(zip(alpha,testc))

# for key in alpha_cipher_pair:
    # alpha_cipher_pair[key] = ord(alpha_cipher_pair[key])
# cipher_alpha_pair = {y:x for x,y in alpha_cipher_pair.items()}    

print(translateCUS(alpha_cipher_pair, test))

print(detranslateCUS(alpha_cipher_pair, translateCUS(alpha_cipher_pair, test)))

# print(cipher_alpha_pair)

# print((test.translate(alpha_cipher_pair)).translate(cipher_alpha_pair))
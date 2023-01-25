user_text = 'Listen, Mr.Jones, calm down.!'

char_count = 0
for character in user_text:
    if (character != ' ') and (character != '.') and (character != ',') and (character != '!'):
        char_count += 1

print(char_count)
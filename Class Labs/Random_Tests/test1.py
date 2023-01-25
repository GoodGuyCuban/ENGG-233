my_pets = ['Dog','Cat','Bird']

for (index, value) in enumerate(my_pets):
    for num in range(0, 5):
        print('{} #{}{}'.format(value, index, num))
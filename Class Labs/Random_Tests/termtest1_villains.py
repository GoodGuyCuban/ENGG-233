# ENDG 233 F21 - Term Test #1 Written Response (9 marks)
# Marcos Perez

# The following program accepts the input of a movie villain and searches a dictionary database to find their corresponding movie title.
# If the villain is in the database, the movie title is printed.
# If the villain is not in the database, they are added, along with their input movie title.
# The program will also print out the number of villains currently in the database each time a transaction is completed.
# The program must also print out a list of all movie titles in the database without repeating duplicate titles.
# The main code is already implemented. 
# A screenshot of example input/output has been provided.

# TASKS:
# Complete the functions print_all and lookup_title. Read through their docstrings to learn more about the functions.
# One line of functionality is missing in the main section. Write a single line of code at the designated position to complete the logic.
# You may not modify any of the given code.


def print_all(villains):
    """
    Prints all unique titles currently held in the dictionary. No titles are duplicated in the printout.

    Arguments:
    villains -- dictionary mapping a villain name string to a movie title string

    Returns:
    None
    
    """
    villains_set = set(villains.values())
    print(villains_set)

    # Delete this line and add your code here. (3 marks)

def lookup_title(char_name, villain_dict):
    """
    Searches the provided dictionary to find the movie title that matches the desired villain name.

    Arguments:
    char_name -- string representing the villain name input by the user
    villain_dict -- dictionary mapping a villain name string to a movie title string

    Returns:
    Returns the corresponding movie title string if a match is found, otherwise returns the string 'Villain not found'
    
    """
    for x in villain_dict:
        if char_name == x:
            return villain_dict[x]
    return 'Villain not found'    # Delete this line and add your code here. (2 marks)



# Starting database defintion.
villains = {
    'Ursula' : 'The Little Mermaid',
    'Mother Gothel' : 'Tangled',
    'Flotsam' : 'The Little Mermaid',
    'Zurg' : 'Toy Story',
    'Maleficent' : 'The Sleeping Beauty',
    'Hans' : 'Frozen',
    'Dr. Facilier' : 'The Princess and the Frog',
    'Scar' : 'The Lion King',
    'Hades' : 'Hercules',
    'Jafar' : 'Aladdin',
    'Sid' : 'Toy Story',
    'Clayton' : 'Tarzan',
    'Cruella De Vil' : '101 Dalmatians',
    'Syndrome' : 'The Incredibles',
    'Captain Hook' : 'Peter Pan',
    'Horace' : '101 Dalmatians',
    'Frollo' : 'The Hunchback of Notre Dame'
}

# Initialize villain input
input_villain = -1

# Continuous input loop
while(input_villain != '0'):
    print('\nThere are {} villains stored in the database.'.format(len(villains)))
    input_villain = input('Enter the name of a villain or select 0 to end: ')

    if input_villain != '0':
        lookup_result = lookup_title(input_villain, villains)    # Call the lookup_title function

        if(lookup_result != 'Villain not found'):
            print('{} is a villain in the movie "{}".'.format(input_villain, lookup_result))    # If villain is found, print their movie title
        else:
            new_movie = input('Villain entry not found. Please enter the name of the villain\'s movie: ')
            ### Write a single line of code here that will add a new entry to the dictionary. (1 mark) ###
            villains[input_villain] = new_movie
            print('New villain added.')

        print('\nThere are {} villains stored in the database.'.format(len(villains)))
        print('The current list of movies in the database is: ')
        print_all(villains)     # Call the print_all function


# Successful execution will be worth an additional 3 marks.

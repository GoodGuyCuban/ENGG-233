# school_data.py
# Marcos Perez, ENDG 233 F21
# A terminal-based application to process and plot data based on given user input and provided csv files.
# You may only import numpy, matplotlib, and math. 
# No other modules may be imported. Only built-in functions that support compound data structures, user entry, or casting may be used.
# Remember to include docstrings for any functions/classes, and comments throughout your code.

#NOTE: As well as the modules below, you will need to ensure openpyxl is installed, as that is the engine pandas uses to interpret xlsx files.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# The following class is provided and should not be modified.
class School:
    """A class used to create a School object.

        Attributes:
            name (str): String that represents the school's name
            code (int): Integer that represents the school's code
    """

    def __init__(self, name, code):
        self.name = name 
        self.code = code

    def print_all_stats(self):
        """A function that prints the name and code of the school instance.

        Parameters: None
        Return: None

        """
        print("School Name: {0}, School Code: {1}".format(self.name, self.code))

def data_process(dataset, schoolcode, year):
    """A function that returns the value in the inputed data set, 
    corrosponding to the inputed schoolcode and year.

    Parameters: Dataset, Schoolcode, year
    Return: Integer value

    """
    return int(dataset[School_Codes_list.index(schoolcode)+1][year])

# Import data here
# Hint: Create a dictionary for all school names and codes
# Hint: Create a list of school codes to help with index look-up in arrays
# NOTE: Pandas is used to import the data, but it is immediately converted to a numpy array, as specified in the assignment outline.
School_Data_2019 = pd.read_csv(r'C:\Users\marco\OneDrive - University of Calgary\Engineering First Year\Endg 233\Portfolio Assignments\Portfolio Projects\proj3data\SchoolData_2018-2019.csv', sep=',',header=None).to_numpy()
School_Data_2020 = pd.read_csv(r'C:\Users\marco\OneDrive - University of Calgary\Engineering First Year\Endg 233\Portfolio Assignments\Portfolio Projects\proj3data\SchoolData_2019-2020.csv', sep=',',header=None).to_numpy()
School_Data_2021 = pd.read_csv(r'C:\Users\marco\OneDrive - University of Calgary\Engineering First Year\Endg 233\Portfolio Assignments\Portfolio Projects\proj3data\SchoolData_2020-2021.csv', sep=',',header=None).to_numpy()
School_Names_Data = pd.read_excel(r'C:\Users\marco\OneDrive - University of Calgary\Engineering First Year\Endg 233\Portfolio Assignments\Portfolio Projects\proj3data\SchoolNames.xlsx',  sheet_name=0).to_numpy()

School_Names_dict = dict(zip(School_Names_Data[:,0].flatten(), School_Names_Data[:,1].flatten())) # Creating dictionary of the Schoolnames with the Schoolcodes as keys.
School_Codes_list = list(School_Names_Data[:,0].flatten()) # Creating a list of Schoolcodes.


# Add your code within the main function. A docstring is not required for this function.
def main():
    print("ENDG 233 School Enrollment Statistics\n")
    
    # Print array data here
    print('\nArray data for 2018 - 2019:')
    print(np.delete(School_Data_2019, 0, axis=0))
    print('Array data for 2019 - 2020:')
    print(np.delete(School_Data_2020, 0, axis=0))
    print('Array data for 2020 - 2021:')
    print(np.delete(School_Data_2021, 0, axis=0))
    
    # Add request for user input here
    valid = 0 
    while(valid == 0): # Input loop, allows program to continue if input is valid
        input1 = input('Please enter the high school name or school code: ')
        if input1 in str(School_Codes_list): # Checks if input is valid, if Schoolname is entered instead of Schoolcode, will convert the input to its Schoolcode

            input1 = int(input1)
            valid += 1

        elif input1 in str(School_Names_dict): 
        
            input1 = int([key for (key, val) in School_Names_dict.items() if input1 == val][0])
            valid += 1

        else:

            print('You must enter a valid school name or code.')
    


    print("\n***Requested School Statistics***\n")

    # Print school name and code using the given class
    # Add data processing and plotting here
    (School(School_Names_dict[input1],input1)).print_all_stats() # Uses provided function to print stats from the selected school.

    enrollmentGR10_2019 = data_process(School_Data_2019, input1, 1) # Creating variables for the mean calculation.
    enrollmentGR11_2019 = data_process(School_Data_2019, input1, 2)
    enrollmentGR12_2019 = data_process(School_Data_2019, input1, 3)
    
    enrollmentGR10_2020 = data_process(School_Data_2020, input1, 1)
    enrollmentGR11_2020 = data_process(School_Data_2020, input1, 2)
    enrollmentGR12_2020 = data_process(School_Data_2020, input1, 3)
    
    enrollmentGR10_2021 = data_process(School_Data_2021, input1, 1)
    enrollmentGR11_2021 = data_process(School_Data_2021, input1, 2)
    enrollmentGR12_2021 = data_process(School_Data_2021, input1, 3)

    print('Mean enrollment for grade 10:\t'+str((int(enrollmentGR10_2019)+int(enrollmentGR10_2020)+int(enrollmentGR10_2021))//3)) # Calculates and prints mean
    print('Mean enrollment for grade 11:\t'+str((int(enrollmentGR11_2019)+int(enrollmentGR11_2020)+int(enrollmentGR11_2021))//3))
    print('Mean enrollment for grade 12:\t'+str((int(enrollmentGR12_2019)+int(enrollmentGR12_2020)+int(enrollmentGR12_2021))//3))
    print('Total number of students who graduated in the past three years:\t'+str(enrollmentGR12_2019 + enrollmentGR12_2020 + enrollmentGR12_2021)) # Calculates and prints total student graduating

    x = [10,11,12] # Creating list for x - axis in graph
    plt.plot(x,[enrollmentGR10_2021, enrollmentGR11_2021,enrollmentGR12_2021], 'bo', label = '2021 Enrollment') # Creating the three lines for the graph using the previously created variables.
    plt.plot(x,[enrollmentGR10_2020, enrollmentGR11_2020,enrollmentGR12_2020], 'go', label = '2020 Enrollment')
    plt.plot(x,[enrollmentGR10_2019, enrollmentGR11_2019,enrollmentGR12_2019], 'ro', label = '2019 Enrollment')
    plt.legend()
    plt.title('Grade Enrollment by Year')
    plt.xlabel('Grade Level')
    plt.ylabel('Number of Students')
    plt.xticks(np.arange(min(x), max(x)+1, 1.0)) # Setting ticks to match the provided example.
    plt.show()

# Do not modify the code below
if __name__ == '__main__':
    main()


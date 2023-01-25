# final_proj.py
# A GUI-based program that allows for the calculation and display of statistics about countries' population, area, and threatened species
# Chris Tiessen, Marcos Perez  ENDG 233 Fall 2021, Block 5
# See the Read_for_GUI_Instructions document for instruction on how to operate the GUI if needed

import PySimpleGUI as sg
import os.path
import numpy as np
import matplotlib.pyplot as plt


#This block creates the basic structure of the file list column in window

file_list_column = [ # Basically, all the gui stuff is done through nested lists, which form the skeleton of the gui before it is activated in the main function. 
#The following two lists represent the two half's of the main screen, the third puts them together.
            [
                sg.Text("CSV Folder"),
                sg.In(size=(25,1), enable_events=True, key="-FOLDER-"),
                sg.FolderBrowse(),
            ],
            [
                sg.Listbox(
                    values=[], enable_events=True, size=(40,20),
                    key="-FILE LIST-"
                )
            ],
        ]

#This block creates the basic structure of the csv column in window

csv_viewer_column = [
    [sg.Text("Choose a CSV file from the list on the left:")],
    [sg.Text(size=(40,1), key="-TARGETNAME-", text='No document selected')],
    [sg.Button('Import'), sg.Button('Search'), sg.Button('Graph'), sg.Button('Check Stats')],
    [sg.HSeparator()],
    [sg.Listbox(
        values=[], size=(20,10),
        key="-IMPORT LIST-"
    )]
]

#This block pieces together the two previous blocks into one window

layout = [
    [
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(csv_viewer_column),
    ]
]

class country_stats:

    '''

    Country_stats contains calculated statistics for countries

    Arguments:

    index(int) = index value of the country being initialized into the class
    Population data array = numpy array containing population data for all countries
    Country_data_array = numpy array containing country data fior all countires
    Specieis_data_array = numpy array containing data about threatened species for all countries

    Attributes:

    name(str) = the name of the country corresponding to the given index
    avg_pop__growth(int) = the average growth of the population over the period of 2000-2021
    pop_per_square_km (int) = the population per square km based on current population (2021) for the given country
    max_pop_2000_2021 (int) = the maximum population of the country between the years 2000-2021
    min_pop_2000_2021 (int) = the minimum population of the country between the years 2000-2021
    change_in_pop_2000_2021 (int) = the change in population of the country between the years 2000-2021
    total_threatened_species(int) = the total number of threatened species in the country
    threatened_species_per_kmsq (float) = the number of threatened species per square kilometer in the country
    threatened_species_per_current_pop (float) = the number of threatened species per current population (2021) in the country

    '''

    def __init__ (self, index, Population_data_array, Country_data_array, Species_data_array):
        
        # Replaces empty data points for countries with no square km data with 1, this makes them easily identifiable
        for i in range(0, len(Country_data_array)):
            if Country_data_array[i][3] == '':
                Country_data_array[i][3] = 1
        
        self.name = Country_data_array[index][0]
        self.avg_pop_growth = (int(Population_data_array[index][21]) - int(Population_data_array[index][1]))/21

        #Replaces the normally calculated value for self.pop_per_sqare_km with 'No Data' for countries labelled with a 1
        if int(Country_data_array[index][3]) == 1:
            self.pop_per_square_km = 'No Data'
        else:
            self.pop_per_square_km = (int(Population_data_array[index][21]))/(int(Country_data_array[index][3])) 

        self.current_pop = Population_data_array[index][21]
        
        #Organises the population data for a given index into a list
        population_numbers = []
        for i in range(1,22):
            population_numbers.append(Population_data_array[index][i])
        population_numbers_array = np.array(population_numbers)

        #Calculates Min and Max using numpy method as required twice
        self.max_pop_2000_2021 = np.max(population_numbers_array.astype(int))
        self.min_pop_2000_2021 = np.min(population_numbers_array.astype(int))
        self.change_in_pop_2000_2021 = int(Population_data_array[index][21]) - int(Population_data_array[index][1])

        self.total_threatened_species = int(Species_data_array[index][1]) + int(Species_data_array[index][2]) + int(Species_data_array[index][3]) + int(Species_data_array[index][4])

        if int(Country_data_array[index][3]) == 1:
            self.threatened_species_per_kmsq = 'No Data'
        else:
            self.threatened_species_per_kmsq = (int(Species_data_array[index][1]) + int(Species_data_array[index][2]) + int(Species_data_array[index][3]) + int(Species_data_array[index][4]))/(int(Country_data_array[index][3])) # check
        self.threatened_species_per_current_pop = (int(Species_data_array[index][1]) + int(Species_data_array[index][2]) + int(Species_data_array[index][3]) + int(Species_data_array[index][4]))/(int(Population_data_array[index][21]))

    def print_all_stats(self):

        """
        print_all_stats displays all attribute stats of the country stored in the class on the GUI

        parameters : none
        returns : none
        
        """
        sg.Window(title='Output',layout=[[sg.Text('Country: '+str(self.name))],[sg.Text('Average population growth: '+str(self.avg_pop_growth))],[sg.Text('Population per square km: '+str(self.pop_per_square_km))],\
            [sg.Text('Current population: '+str(self.current_pop))],[sg.Text('Maximum population (2000-2021): '+str(self.max_pop_2000_2021))],[sg.Text('Minimum population (2000-2021): '+str(self.min_pop_2000_2021))],\
                [sg.Text('Change in population (2000-2021): '+str(self.change_in_pop_2000_2021))],[sg.Text('Total threatened species: '+str(self.total_threatened_species))],[sg.Text('Threatened species per square km: '+str(self.threatened_species_per_kmsq))],\
                    [sg.Text('Threatened species per current population: '+str(self.threatened_species_per_current_pop))]],margins=(100,5)).read()


window = sg.Window("ENDG 233 Statistics Project", layout) # Creating the window object with the previously established layout


def selection_check(window_local):

    """
    This function checks if a document/file is currently being selected

    Parameters: 
    window_local - gui windows filetype, used to check if something is being selected
    
    Returns:
    Boolean - True or False

    """

    if window_local["-TARGETNAME-"].get() != 'No document selected':
        return True
    else:
        sg.Window(title='Error',layout=[[sg.Text("No document selected")]],margins=(100,1)).read()
        return False


def error_prompt(error_message):

    """

    This function prompts a window with an error message
    
    Parameters: 
    
    error_message - String that is desired error message for user

    Returns: none

    """

    sg.Window(title='Error',layout=[[sg.Text(error_message)]],margins=(100,1)).read()

def graphing_function_population(selected_data_list, Population_data_array, Country_data_array):

    """
    This function graphs population density for a list of selected countries

    Parameters:

    selected_data_list  = list of the indexes of selected countries for graphing
    Population_data_array = numpy array of the population data sheet
    Country_data_array = numpy array of the country data sheet

    Returns:

    none
    
    """
    # replaces all of the empty data slots for square kilometers in the provided data with a 1 so easily identifiable 

    for i in range(0, len(Country_data_array)):
        if Country_data_array[i][3] == '':
            Country_data_array[i][3] = '1'
            Country_data_array[i][0] = (f'{Country_data_array[i][0]} - No Data')

    # creates the lists for graphing, ensures that No Data is shown for the countries previously identfied with a 1

    data_labels = [Country_data_array[i][0] for i in selected_data_list]
    population_density_list = [0 if Country_data_array[i][3] == '1' else (int(Population_data_array[i][21])/int(Country_data_array[i][3])) for i in selected_data_list]
    
    #Creates the graph

    plt.figure(1)
    plt.bar(data_labels, population_density_list, color = 'maroon', width = 0.4, label = 'Population Density')
    plt.xticks(rotation = 'vertical', size = 6)
    plt.title('Population Density for Countries in the Given Area', size = 14)
    plt.xlabel('Countries')
    plt.ylabel('Current Population density (People per square km)')
    plt.legend()

    plt.show()

def search_function_country_data(search_term, selected_array):

    """
    Searches the Country Data imported sheet for regions, subregions, countries, and returns a list of the indexes applying to the given search term

    Parameters:
    Search term (str): the specified term through which to filter the numpy array of country data
    selected_array : the numpy array to search

    Returns:
    indicies_of_selected_data (list) : list containing the indices of the selected countries based on the search term used

    """
    
    Country_data_array = selected_array
    indicies_of_selected_data = []
    for i in range(0,195):
        if search_term == Country_data_array[i][0] or search_term == Country_data_array[i][1] or search_term == Country_data_array[i][2] or search_term == Country_data_array[i][3]:
            indicies_of_selected_data.append(i)
    if indicies_of_selected_data == []:
        indicies_of_selected_data = 'No value found'
    return indicies_of_selected_data    

def graphing_function_animal(selected_data_list, Population_data_array, Country_data_array, Species_data_array):

    """
    This function graphs threatened species per the current population for a list of selected countries

    Parameters:

    selected_data_list  = list of the indexes of selected countries for graphing
    Population_data_array = numpy array of the population data sheet
    Country_data_array = numpy array of the country data sheet
    Species_data_array = numpy array of the threatened species data sheet

    Returns:

    none
    
    """
    # Creates the lists for graphing

    data_labels = [Country_data_array[i][0] for i in selected_data_list]
    avg_threatened_species_per_current_population = [(int(Species_data_array[i][1])+int(Species_data_array[i][2])+int(Species_data_array[i][3])+int(Species_data_array[i][4]))/(int(Population_data_array[i][21])) for i in selected_data_list]

    # Creates the graph
    
    plt.figure(2)
    plt.bar(data_labels, avg_threatened_species_per_current_population, color = 'orange', width = 0.4, label = 'Threatened Species per Population')
    plt.xticks(rotation = 'vertical', size = 6)
    plt.title('Threatened species per Current Population for Given Region', size = 14)
    plt.xlabel('Countries')
    plt.ylabel('Threatened Species per Given Population')
    plt.legend()

    plt.show()


"""
Main function
"""
def main():
    # Creating variables
    selection_list = []
    array1 = []
    array2 = []
    array3 = []
    array1_name = ''
    array2_name = ''
    array3_name = ''
    arraydict = {}

    while True:
        event, values = window.read() # Activates and reads the menu

        if event == "Exit" or event == sg.WIN_CLOSED: # Breaks out of the loop if the window has been closed
            break

        if event == "-FOLDER-": # If a folder has been selected, this block will update the file list to show a list of compatible files
            folder = values["-FOLDER-"]
            try:
                file_list = os.listdir(folder)
            except:
                file_list = []

            fnames = [
                f for f in file_list if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith((".csv"))
            ]
            window["-FILE LIST-"].update(fnames)
        
        if event == "Import": # If the import button is pressed, this block will check if the array variables are empty, and will fill them and add them to the selection list accordingly
            if values["-FILE LIST-"]:
                if len(selection_list) < 3: # Ensures that there are not 3 items already imported
                    if np.array(array1).size == 0 and values["-FILE LIST-"][0] not in selection_list: # Imports document into first available array slot and assigns the array to a dictionary for easy access later (same for the two other statements following) 
                        array1 = np.genfromtxt(os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0]), dtype = str, delimiter=',')
                        array1_name = values["-FILE LIST-"][0]
                        arraydict[array1_name] = array1

                    elif np.array(array2).size == 0 and values["-FILE LIST-"][0] not in selection_list:
                        array2 = np.genfromtxt(os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0]), dtype = str, delimiter=',')
                        array2_name = values["-FILE LIST-"][0]
                        arraydict[array2_name] = array2

                    elif np.array(array3).size == 0 and values["-FILE LIST-"][0] not in selection_list:
                        array3 = np.genfromtxt(os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0]), dtype = str, delimiter=',')
                        array3_name = values["-FILE LIST-"][0]
                        arraydict[array3_name] = array3

                    selection_list.append(values["-FILE LIST-"][0]) # updates the list to track the amount of files already imported
                    selection_list = list(set(selection_list)) # checks for duplicates
                    
                    window["-IMPORT LIST-"].update(selection_list)
                else:
                    error_prompt('Already Imported Max. 3')
            else:
                error_prompt('Please select folder first')
        
        if event == "Search": # If the search button is pressed, this block will check if a valid file is being selected, and if so, will search the file by calling the search function

            is_valid = selection_check(window)
            if is_valid == True: # checks if a selection is made
                window2 = sg.Window(title='Selection',layout=[[sg.Text("Provide a desired term")],[sg.Input(key = '-HEADER INPUT-'),sg.Button('OK')]],margins=(100,1))
                event1, values1 = window2.read()
                if event1 == 'OK':
                    window2.close()
                input_header = values1['-HEADER INPUT-']

                if values["-IMPORT LIST-"][0] == array1_name: # calls the search function on whichever array is being selected
                    sg.Window(title='Index of Term(s)',layout=[[sg.Text(search_function_country_data(input_header, array1))]],margins=(100,1)).read()
                    
                elif values["-IMPORT LIST-"][0] == array2_name:
                    sg.Window(title='Index of Term(s)',layout=[[sg.Text(search_function_country_data(input_header, array2))]],margins=(100,1)).read()

                elif values["-IMPORT LIST-"][0] == array3_name:
                    sg.Window(title='Index of Term(s)',layout=[[sg.Text(search_function_country_data(input_header, array3))]],margins=(100,1)).read()

                else:
                    error_prompt('Please select a valid file')

        if event == "Graph": # If the graph button is pressed, this block will identify the selected file, and then run the appropriate graph function for said file, if an invalid file is selected, it will prompt the user
            if values["-IMPORT LIST-"]:
            
                if values["-IMPORT LIST-"][0] == 'Population_Data.csv': # detects what type of csv file is being selected
                    window2 = sg.Window(title='Selection',layout=[[sg.Text("Enter a country, subregion, or region")],[sg.Input(key = '-SELECTED TERM-'),sg.Button('OK')]],margins=(100,1))
                    event1, values1 = window2.read()

                    if event1 == 'OK': 
                        window2.close()

                    if 'Country_Data.csv' in arraydict: # checks to see if the requisite data file has been imported
                        if values1['-SELECTED TERM-'] in arraydict['Country_Data.csv'] and len(selection_list) == 3: # calls a graphing function depending on what file is being selected
                            region_indexes = search_function_country_data(values1['-SELECTED TERM-'], arraydict['Country_Data.csv'])
                            countries_in_region = [arraydict['Country_Data.csv'][int(x)][0] for x in region_indexes]
                            graphing_function_population(region_indexes, arraydict['Population_Data.csv'], arraydict['Country_Data.csv'])

                        else:
                            error_prompt('Please enter a valid region')
                
                    else:
                        error_prompt('Please import a valid file')
                    

                elif values["-IMPORT LIST-"][0] == 'Threatened_Species.csv': # detects what type of csv file is being selected
                    window2 = sg.Window(title='Selection',layout=[[sg.Text("Enter a country, subregion, or region")],[sg.Input(key = '-SELECTED TERM-'),sg.Button('OK')]],margins=(100,1))
                    event1, values1 = window2.read()

                    if event1 == 'OK':
                        window2.close()

                    if 'Country_Data.csv' in arraydict: # checks to see if the requisite data file has been imported
                        if values1['-SELECTED TERM-'] in arraydict['Country_Data.csv'] and len(selection_list) == 3: # calls a graphing function depending on what file is being selected
                            region_indexes = search_function_country_data(values1['-SELECTED TERM-'], arraydict['Country_Data.csv'])
                            countries_in_region = [arraydict['Country_Data.csv'][int(x)][0] for x in region_indexes]
                            graphing_function_animal(region_indexes, arraydict['Population_Data.csv'], arraydict['Country_Data.csv'], arraydict['Threatened_Species.csv'])

                        else:
                            error_prompt('Please enter a valid region')
                
                    else:
                        error_prompt('Please import a valid file') # error prompts for failed cases
                else:
                    error_prompt('Please select a valid file')
            else:
                error_prompt('Please import a document')    

        if event == "Check Stats": # If the check stats button is pressed, this block will prompt the user for a region, check if the input is valid, prompt a user with a list of contries in that region, then call on the stats class to output a summary window with manipulated data.
            window2 = sg.Window(title='Selection',layout=[[sg.Text("Enter a region")],[sg.Input(key = '-REGION-'),sg.Button('OK')]],margins=(100,1))
            event1, values1 = window2.read()

            if event1 == 'OK':
                    window2.close()

            if 'Country_Data.csv' in arraydict: # checks to see if the requisite data file has been imported
                
                if values1['-REGION-'] in arraydict['Country_Data.csv'][:,1] and len(selection_list) == 3: # checks if the input exists and is valid
                    region_indexes = search_function_country_data(values1['-REGION-'], arraydict['Country_Data.csv'])
                    countries_in_region = [arraydict['Country_Data.csv'][int(x)][0] for x in region_indexes]

                    window2 = sg.Window(title='Selection',layout=[[sg.Listbox(values=countries_in_region, size=(40,20),key="-COUNTRY LIST-"),sg.Button('OK')]],margins=(100,1))
                    event1, values1 = window2.read()
                    if event1 == 'OK':
                        country_stats(int(np.where(arraydict['Country_Data.csv'] == values1['-COUNTRY LIST-'][0])[0]), arraydict['Population_Data.csv'], arraydict['Country_Data.csv'], arraydict['Threatened_Species.csv']).print_all_stats()
                        window2.close()
                else:
                    error_prompt('Please enter a valid region')
                
            else:
                error_prompt('Please import a valid file')
            
        elif event == "-FILE LIST-": # If the a file in the file list is selected, this block will update the target name string on the right side of the gui
            try:
                filename = os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0])
                window["-TARGETNAME-"].update(filename)
                
            except:
                pass
        
    window.close() # Closes window 
        
if __name__ == '__main__':
    main() 
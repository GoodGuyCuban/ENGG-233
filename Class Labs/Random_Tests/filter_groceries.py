# ENDG 233 F21 - Term Test #2 Written Response (5 marks)
# ADD YOUR NAME HERE


# INSTRUCTIONS:
# The following program should allow you to filter a dictionary based on given parameters.
# The main code is already implemented. 
# You must complete the function filter_groceries without changing the function definition.
# You must use a list or dictionary comprehension to do the filtering.
# A screenshot of example input/output has been provided.
# You may not modify any of the given code or add code outside of the filter_groceries function.


def filter_groceries(lower, upper, groceries):
    """This function filters a given dictionary based on the provided upper and lower bounds.

    Args:
        lower (float): Lower price limit
        upper (float): Upper price limit
        groceries (dict): A dictionary that maps grocery items to their price.

    Returns:
        dict: Returns a dictionary that only contains key-value pairs where the value is within or equal to the specified bounds.
    """

    return {i : x for (i , x) in groceries.items() if x >= lower and x <= upper} #ONE LINE, BABY!



# Main code begins here
print('ENDG 233 Term Test #2\n')

# Grocery dictionary
grocery_prices = {'Strawberries':5.00,'Apples':3.00,'Lemons':1.00,'Pears':4.50,'Cucumbers':2.00,'Brussel Sprouts':3.50,'Garlic':6,'Tomatoes':3.75,'Oranges':3.00,'Potatoes':2.00}

# Returned dictionary should include all key:value pairs where the value is within or equal to the given limits.
highest_price = 4.00
lowest_price = 2.50

# Function call
print(filter_groceries(lowest_price, highest_price, grocery_prices))

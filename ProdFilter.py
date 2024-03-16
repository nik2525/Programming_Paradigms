# Define a function that filters product names with length greater than or equal to 5
def filter_long_names(product_names):
    long_names = []  # Initialize an empty list to store the filtered product names
    for name in product_names:  # Loop through each product name in the input list
        if len(name) >= 5:  # Check if the length of the current name is greater than or equal to 5
            long_names.append(name)  # If so, append the name to the list of filtered names
    return long_names  # Once all names have been checked, return the list of filtered names

# Define a list of product names
product_names = ["Shirt", "Headphones", "Monitor", "Cable"]

# Call the filter_long_names function with the list of product names as an argument
long_names = filter_long_names(product_names)

# Print the list of filtered product names
print(long_names)  # Output: ['Shirt', 'Headphones', 'Monitor']


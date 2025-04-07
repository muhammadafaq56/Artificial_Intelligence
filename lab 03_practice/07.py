# Create a list with various data types
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]

# Loop through each item in the list
for item in datalist:
    # Print the item and its data type
    print(f"Item: {item}, Type: {type(item)}")

from max_min_select import find_max_min
from input_handler import get_array_input

# User enters the elements of the array
arr = get_array_input()

# Call the function to find the maximum and minimum elements
min_element, max_element = find_max_min(arr)

# Show the results - 
print(f"Minimum element: {min_element}")
print(f"Maximum element: {max_element}")

def get_array_input():
    # user enters the number of elements in the array
    n = int(input("Type the quantity of elements in the array: "))

    if( n < 0):
        print("The number of elements must be greater than 0")
        return get_array_input()
    
    # create an empty array
    arr = []
    
    # user enters the elements of the array
    for i in range(n):
        elem = float(input(f"Type the {i+1}º element: "))  # using float to allow decimal numbers
        arr.append(elem)
    
    return arr

# MaxMin Select Algorithm

This project implements the MaxMin Select algorithm, which finds both the maximum and minimum elements in an array using the divide and conquer approach. It was developed to practice algorithmic design and recursion.

# About

The MaxMin Select algorithm efficiently finds the maximum and minimum elements in a sequence by dividing the sequence into two halves and recursively finding the min and max for each half. The final results are then combined to determine the overall min and max.

# Run

1. This project was developed in Python 3, so you need to have Python installed on your machine to run the code. You can follow this [tutorial](https://code.visualstudio.com/docs/python/python-tutorial) to get started.

2. Clone this repository.

3. After that, to run the code, use the following command in the repository root:

```
python3 main.py
```

# Testing

To run the tests, you can use Python's built-in `unittest` framework.

1. To execute the tests, run the following command in the root directory of the project:

```
python3 -m unittest test_max_min_select.py
```

This will run all the test cases in the `test_max_min_select.py` file.

# Structure

This repository contains the following `.py` files:

- **`max_min_select.py`**: Implements the recursive MaxMin Select algorithm.
- **`input_handler.py`**: Handles the user input to dynamically create the array.
- **`main.py`**: Contains the main function that drives the program and displays the results.
- **`test_max_min_select.py`**: Contains test cases for the MaxMin Select algorithm.

# Explanation of the Algorithm

### **Function Definition (`max_min_select.py`)**

```python
def max_min_select(arr, low, high):
```
- Defines the function `max_min_select(arr, low, high)`, which takes a list `arr` and the indices `low` and `high` to process a sublist and returns the minimum and maximum of that sublist using recursion.

### **Base Case**

```python
if low == high:
    return arr[low], arr[low]
```
- If the sublist has only one element, it returns that element as both the min and max.

### **Two Elements Case**

```python
if high == low + 1:
    if arr[low] > arr[high]:
        return arr[high], arr[low]
    else:
        return arr[low], arr[high]
```
- If there are exactly two elements, it directly compares them and returns the smaller and larger values.

### **Recursive Division**

```python
mid = (low + high) // 2
min1, max1 = max_min_select(arr, low, mid)
min2, max2 = max_min_select(arr, mid + 1, high)
```
- Recursively divides the list into two halves and computes the min and max for each half.

### **Combining the Results**

```python
final_min = min(min1, min2)
final_max = max(max1, max2)
return final_min, final_max
```
- Combines the results from both halves and returns the overall min and max.

---

### **Main Function (`main.py`)**

```python
from max_min_select import find_max_min
from input_handler import get_array_input

def main():
    arr = get_array_input()
    min_element, max_element = find_max_min(arr)
    print(f"Minimum element: {min_element}")
    print(f"Maximum element: {max_element}")
```

### **Explanation**
- **Imports** the `find_max_min` function from `max_min_select.py` and `get_array_input` from `input_handler.py`.
- Defines `main()`, which:
  1. Prompts the user to input an array.
  2. Finds the min and max elements using the `find_max_min` function.
  3. Prints the results.
- Runs `main()` when the script is executed.



# Complexity Analysis of MaxMin Select

## 1. Asymptotic Complexity Analysis Using Operation Counting

### Comparison Counting

1. **Base Case**: If there is only one element in the array, no comparisons are needed.
   - **Comparisons**: **0**.

2. **Two Elements Case**: If there are exactly two elements, one comparison determines the minimum and maximum.
   - **Comparisons**: **1**.

3. **General Case** (More than two elements): The array is divided into two halves, and two recursive calls are made to find the min and max in each half. After recursion, two comparisons are made to merge the results:
   - One to find the overall minimum: **min(min1, min2)**
   - One to find the overall maximum: **max(max1, max2)**
   - **Comparisons**: **2** per recursion level.

### Counting Comparisons per Recursion Level

- **Level 0**: \(2\) comparisons.
- **Level 1**: \(2 x 2 = 4\) comparisons.
- **Level 2**: \(4 x 2 = 8\) comparisons.
- **Level k**: \(2^{k+1}\) comparisons.

Since the recursion depth is log2 n, the total number of comparisons is:


C(n) = 2(n - 1)


## 2. Asymptotic Complexity Using the Master Theorem

The recurrence relation for the algorithm is:

T(n) = 2T(n/2) + O(1)

### Identifying Parameters

- \(a = 2\) (two recursive calls)
- \(b = 2\) (problem size is halved in each recursion step)
- \(f(n) = O(1)\) (constant operations per level)

p = log2 2 = 1

### Applying the Master Theorem

Here, we have:
-  f(n) = O(1), which is equivalent to O(n^0).
- Since \( p = 1 \) and \( 0 < 1 \), we apply **Case 1** of the Master Theorem, resulting in:

T(n) = O(n)


## 3. Conclusion

Both the operation counting method and the Master Theorem indicate that the asymptotic complexity of the algorithm is **O(n)**. This means that the number of operations grows linearly with the input size, making the algorithm efficient for finding the minimum and maximum values in an array.

# References

Understanding more about Divide and Conquer algorithms:
- [Link1](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm)

Understanding Python Recursion:
- [Link1](https://realpython.com/python-recursion/)
- [Link2](https://www.programiz.com/python-programming/recursion)

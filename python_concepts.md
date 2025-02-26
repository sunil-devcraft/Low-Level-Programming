# List comprehension by example
```py
# Sum of two matrix

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

for i in range(len(A)):
    row_result = [];
    for j in range(len(A[0])):
        row_result.append(A[i][j] + B[i][j])
    result.append(row_result)
    
print result
```


*List comprehension is a concise way to create lists in Python. It replaces loops with a single-line expression, making your code shorter and more readable.*

syntax ``[expression for item in iterable if condition]``

```py
# Square of numbers with list comprehension
number  = [1,2,3,4]
pysqr   = [number[i]*number[i] for i in range(len(number))]

print(pysqr)
```

```py
# Sum of two matrix with list comprehension
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))

print(result)
```


Why use list comprehensions?
* Less code
* Faster execution
* More Pythonic (preferred style in Python)
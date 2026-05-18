# NumPy – Methods and Usage

# 1. Creating NumPy Arrays


# Method 1: Creating 1D, 2D, and 3D Arrays

import numpy as np

arr1 = np.array([1,2,3,4,5])
print(arr1)

arr2 = np.array([[1,2,3], [4,5,6]])
print(arr2)

arr3 = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
print(arr3)


# Method 2: Creating Arrays with Specific Values

# Array of zeros
zeros = np.zeros((3, 3))
print(zeros)

# Array of ones
ones = np.ones((2, 4))
print(ones)

# Identity matrix
identity = np.eye(4)
print(identity)


# Array of a specific value
full_array = np.full((2, 3), 7)
print(full_array)   


# Method 3: Generating Ranges of Numbers

# Array with range of numbers
range_arr = np.arange(1, 11, 2)
print(range_arr)

# Linearly spaced values
lin_space = np.linspace(0, 100, 5)
print(lin_space)


# 2. Random Number Generation

# Random integer values
rand_int = np.random.randint(1, 100,(3,3))
print(rand_int)

# Random values between 0 and 1
rand_float = np.random.rand(3, 3)
print(rand_float)

# Standard normal distribution (mean=0, std=1)
rand_norm = np.random.randn(3, 3)
print(rand_norm)

# Random choice from a list
rand_choice = np.random.choice([10,20,30,40,50], 5)
print(rand_choice)

# Setting a random seed (for reproducibility)
np.random.seed(42)
rand = np.random.rand(3, 3)
print(rand)

# Real time Examle Dice Game

player_score = 0
computer_score = 0

for i in range(5):
    print("\nRound", i+1)

    player = np.random.randint(1, 7)
    computer = np.random.randint(1, 7)

    print("You:", player)
    print("Computer:", computer)

    if player > computer:
        print("You win this round!")
        player_score += 1

    elif player < computer:
        print("Computer wins the round!")
        computer_score = +1

    else:
        print("Tie!")

print("\nFinal Score")
print("You:", player_score)
print("Computer:", computer_score)


# Real time Example Generate Lottery Numbers

# Add User Interaction (Better Project)

input("Press Enter to generate your lottery numbers...")

numbers = np.random.choice(range(1, 51), 6, replace = False)
numbres = np.sort(numbers)

print("🎯 Your lottery numbres:", numbres)


# 3. Shape and Reshaping

# Checking shape
arr = np.array([[1,2,3], [4,5,6,]])
print(arr.shape)

# Reshaping an array
reshaped = arr.reshape(3, 2)
print(reshaped)

# Flattening an array (convert to 1D)
flattened = arr.flatten()
print(flattened)


# Transposing a matrix
transposed = arr.T
print(transposed)


# 4. Array Indexing and Slicing


# Accessing elements
arr = np.array([10,20,30,40,50])
print(arr[0])  # First element
print(arr[-1]) # Last element

# Slicing arrays
print(arr[1:4])  # Elements from index 1 to 3
print(arr[:3])   # First 3 elements
print(arr[::2])   # Every second element


# Slicing 2D array
matrix = np.array([[10,20,30], [40,50,60], [70,80,90]])
print(matrix[1, 2])   # Element at row index 1 and column index 2


print(matrix[:, 1])  # All rows, second column
print(matrix[0:2, 1:3]) # Subset of matrix
                

# 5. Mathematical Operations



arr = np.array([1,2,3,4,5])

# Element-wise operations
print(arr + 10)
print(arr * 2)
print(arr ** 2)
print(np.sqrt(arr))

# Basic aggregate functions
print(np.sum(arr))
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))
print(np.min(arr))
print(np.max(arr))

# Cumulative sum and product
print(np.cumsum(arr))
print(np.cumprod(arr))
               

# 6. Boolean Indexing and Filtering


arr = np.array([10,20,30,40,50])

# Boolean indexing
bool_arr = arr > 25
print(bool_arr)   # Returns [False, False, True, True, True]

# Filtering values
filtered_arr = arr[arr > 25]
print(filtered_arr)           # Returns [30, 40, 50]


# 7. Linear Algebra with NumPy

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
print(np.dot(A, B))

# Determinant
print(np.linalg.det(A))

# Inverse
print(np.linalg.inv(A))

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print(eigenvalues)
print(eigenvectors)


# Solving linear equations (Ax = B)
C = np.array([5, 11])
solution = np.linalg.solve(A, C)
print(solution)


# 8. Sorting and Unique Values

arr = np.array([3,1,4,1,5,9,2,6])

# Sorting an array
sorted_arr = np.sort(arr)
print(sorted_arr)

# Unique elements
unique_values = np.unique(arr)
print(unique_values)


# 9. Stacking and Splitting Arrays


A = np.array([[1,2], [3,4]])
B = np.array([[5,6], [7,8]])


# Stacking arrays vertically and horizontally
vertical_stack = np.vstack((A, B))
horizontal_stack = np.hstack((A, B))

print(vertical_stack)
print(horizontal_stack)

# Splitting arrays
split_arr = np.split(np.array([1,2,3,4,5,6]), 3)
print(split_arr)


# 9. Stacking and Splitting Arrays


A = np.array([[1,2], [3,4]])
B = np.array([[5,6], [7,8]])


# Stacking arrays vertically and horizontally
vertical_stack = np.vstack((A, B))
horizontal_stack = np.hstack((A, B))

print(vertical_stack)
print(horizontal_stack)

# Splitting arrays
split_arr = np.split(np.array([1,2,3,4,5,6]), 3)
print(split_arr)



# 10. Copying and Views

arr = np.array([10,20,30])

# Shallow copy (view)
view_arr = arr.view()
view_arr[0] = 100
print(arr)                 # Changes reflect in original array


# Deep copy
copy_arr = arr.copy()
copy_arr[0] = 200
print(arr)              # Original array remains unchanged

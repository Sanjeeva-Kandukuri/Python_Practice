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

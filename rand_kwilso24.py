import random

def random_array(arr):
    for i in range(len(arr)):
        arr[i] = i + 1  # Or any other range of numbers you want
    random.shuffle(arr) # Shuffle the list in-place.
    return arr

#Example usage:
arr = [None]*20
shuffled_array = random_array(arr)
print(shuffled_array)

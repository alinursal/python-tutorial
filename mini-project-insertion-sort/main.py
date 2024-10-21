import random

def insertion_sort(arr):
    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        key = arr[i]  # The current element to be compared
        j = i - 1  # Index of the last sorted element

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # Shift element to the right
            j -= 1
        arr[j + 1] = key  # Place the key at its correct position

def main():

    random_list = random.sample(range(1, 101), 10)  # 10 unique random numbers between 1 and 100

    insertion_sort(random_list)

    print("Sorted list:", random_list)


main()
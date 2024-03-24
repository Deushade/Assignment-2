# Program Name: Merge Sort Visualization

# Program Author: Leigh McElmon

# Program Description: This program implements and showcases merge. It does this by slowly going 
# through the merge sort divide and conquor process and playing a sound for each iterative process
# where a number is placed into a new array. Every time the algorithm merges and divides I also 
# included some outputs highlighting that. At the end of the program, it will output the new
# sorted array using merge sort.

# Importing a library so sound can be used for each 'swap' made
import pygame
# Initializing the python library
pygame.mixer.init()

# Creating a function to play the swap sound from a file called swap_sound using the pygame library
def play_swap_sound():
    pygame.mixer.Sound('swap_sound.mp3').play()
    # This is a useful command for creating tim between each swap iteration for the sound to play
    while pygame.mixer.get_busy(): 
        # Delay so the program can slowly go through the merge sort. Which is through adjusting delay for the sound
        pygame.time.delay(10)

# Creating a function for the recursive merge sort
def merge_sort(arr, depth=0):
    # This is to help format the merge sort so you can visualize the sorting better. Indenting the merges
    indent = "  " * depth 
    # If length of the array is greater than 1
    if len(arr) > 1:
        # Find the middle of the array
        mid = len(arr) // 2 
        # Divides the array elements to a left and right list
        L = arr[:mid]
        R = arr[mid:]

        # Output for the above operations to show the initial array divided
        print(f"{indent}Now Dividing: {arr}")
        # Sorts the left half of the array (left list)
        merge_sort(L, depth + 1)  
        # Sorts the right half of the array (right list)
        merge_sort(R, depth + 1) 

        i = j = k = 0

        # Printing to show the merge operation is about to happen
        print(f"\n{indent}Now Merging: {L} and {R}")
        # While loop to set the conditions for merge sort
        while i < len(L) and j < len(R):
            # Comparison operation with the left and right sub arrays
            if L[i] < R[j]:
                # Smaller number gets placed into the left sub array
                arr[k] = L[i]
                # Move to the next element in the left sub array
                i += 1
            else:
                arr[k] = R[j]
                # Move to the next element in the right sub array
                j += 1
            # Printing the number and the index of it
            print(f"{indent}Selected {arr[k]} for index {k}")
            # play the swap sound when a number is selected for the index
            play_swap_sound()
            k += 1


        while i < len(L):
            arr[k] = L[i]
            print(f"{indent}Selected {L[i]} for index {k}")
            play_swap_sound()
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            print(f"{indent}Selected {R[j]} for index {k}")
            play_swap_sound()
            j += 1
            k += 1

# Main function where the merge sort operation is called. The array can be changed from here with n
# amount of numbers.
def main():
    # An array that can be changed for any merge sort of n numbers
    arr = [4, 3, 2, 1]
    # Printing the array before it's sorted
    print("Given array is:", arr)
    # Calling the merge_sort function so it can be applied to array numbers
    merge_sort(arr)
    # Prints the final sorted array as it's coded after the merge_sort function
    print("Sorted array is:", arr)

# Calling main for the program to run
main()

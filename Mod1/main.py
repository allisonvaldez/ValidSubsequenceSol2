# time: O(n) n represents the length of the array | space: O(1)


def test_valid_subsequence(array, sequent_array):
    # start with creating the sequent starting index
    sequent_index = 0

    # initialize a for loop to traverse the first array for comparison
    for i in array:
        """
         create a stopping case to prevent the algorithm from traversing out of 
         bounds of the sequent array by making sure it does not surpass the 
         length of itself.
         """
        if sequent_index == len(sequent_array):
            break

        """
        create a statement that checks if the sequence array at a particular 
        location matches an index in the first array.
        """
        if sequent_array[sequent_index] == i:
            sequent_index += 1

    """
    Returns true if we found all items in the original array that's equal to the
    length of the sequent array (all items of the sequent array are found).
    """
    return sequent_index == len(sequent_array)


print(test_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
print(test_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [26]))

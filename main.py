def bubbleSort(array):
    """
    A function that takes in a array of intergers and returns a sorted version that array. Making use of the Bubble
    Sort algorithm to sort that array.
    """
    isSorted = False
    while not isSorted:
        isSorted = True
        for idx in range(len(array) - 1):
            if array[idx + 1] < array[idx]:
                swap(idx, idx + 1, array)
                isSorted = False
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
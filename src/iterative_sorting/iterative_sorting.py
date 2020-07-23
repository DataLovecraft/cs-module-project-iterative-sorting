# TO-DO: Complete the selection_sort() function below

def selection_sort(arr):
    # 'i' indicates how many items were sorted
    for i in range(len(arr)):
        # To find the min value of the unsorted segment
        # we assume the the first element is the lowest
        min_idx = i
        # we then use 'j' to loop through the remaining elements
        for j in range(i + 1, len(arr)):
            # update min_idx if the element at j is lower
            if arr[j] < arr[min_idx]:
                min_idx = j
        # after finding the lowest item of the unsorted regions, swap
        # with the first unsorted item
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr



# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    swapped = True    # Ensures the loop runs at least once
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                # swap the elements
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True    # keeps the loop going

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the
buckets.

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    """
    arr -> input array
    position -> temporary array
    result -> sorted array

    """
    #n = len(arr)
    #m =


    return arr

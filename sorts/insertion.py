#My implementation of the insertion sort
def insertion_sort(arr):
    """
    Insertion sort takes an array of unordered numbers and returns an array of all of the numbers in order

    Insertion sort operates under the function that an array of 1 is sorted, and then we go through the index of the list of the rest 
    and we place the value of where it belongs in the already ordered list 
    
    """
    size = len(arr)

    for i in range(1, size):
        #sorts the values from the unsorted part of the array
        for l in range(0, i):
            #goes through the sorted part of the array and finds where the value of arr[i] belongs
            if arr[i] < arr[l]:
                temp = arr[l]
                arr[l] = arr[i]
                arr[i] = temp
    
    return arr




arr = [-4,4,0,5,24,333,45,66,21,563]

print (insertion_sort(arr))
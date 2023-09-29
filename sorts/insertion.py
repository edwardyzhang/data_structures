#My implementation of the insertion sort
def insertion_sort(arr):
    """
    Insertion sort takes an array of unordered numbers and returns an array of all of the numbers in order

    Insertion sort operates under the function that an array of 1 is sorted, and then we go through the index of the list of the rest 
    and we place the value of where it belongs in the already ordered list 
    
    Takes O(n^2) time with n elements 
    
    """
    size = len(arr)

    for i in range(1, size):
        #sorts the values from the unsorted part of the array
        
        for l in range(0, i):
            #goes through the sorted part of the array and finds where the value of arr[i] belongs
            if arr[i] > arr[l]:
                temp = arr[l]
                arr[l] = arr[i]
                arr[i] = temp
                #since the sort found where the value was supposed to be, there is no need to check the rest of the array
                continue
    
    return arr

def selection_sort(arr):
    """
    This sorting algorithm goes through the list and finds the small number and places it at the front of the array
    
    """
    size = len(arr)
    
    for i in range(size):
        #using the placeholder of the first number as the smallest
        #goes through the array of [i:max] and sees if there is any other smaller number than it
        smallest = i
        for l in range(i, size):
            #once it finds a smaller number, the algo remembers which index is it
            if arr[l] < arr[smallest]:
                smallest = l
                
        #swaps the index with the smallest number
        temp = arr[i]
        arr[i] = arr[smallest]
        arr[smallest] = temp
    
    return arr 

def merge_sort(arr):
    """
    This sorting algorithm divides the array into smaller arrays and then recursively sorts those smaller array and combines them
    
    """
arr = [4,0,-4,5,24,333,45,66,21,563]

print (selection_sort(arr))
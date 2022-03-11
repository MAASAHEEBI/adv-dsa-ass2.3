#3)Implement Quick Sort


def quicksort(arr, start, end):
    
    if end - start > 1:
        p = partition(arr, start, end)
        quicksort(arr, start, p)
        quicksort(arr, p + 1, end)
 
 
def partition(arr, start, end):
    pivot = arr[start]
    i = start + 1
    j = end - 1
 
    while True:
        while (i <= j and arr[i] <= pivot):
            i = i + 1
        while (i <= j and arr[j] >= pivot):
            j = j - 1
 
        if i <= j:
           arr[i], arr[j] = arr[j], arr[i]
        else:
            arr[start], arr[j] = arr[j], arr[start]
            return j
 
 
arr = input('Enter the numbers of list to be Sort with space between them: ').split()
arr = [int(x) for x in arr]
quicksort(arr, 0, len(arr))
print('Sorted list: ', end='')
print(arr)

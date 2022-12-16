def partition(arr, l, r):
    
    pivot = arr[r]
    i = l - 1
    
    for j in range(l, r):
        if arr[j] <= pivot:
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])

    (arr[i + 1], arr[r]) = (arr[r], arr[i + 1])

    return i + 1
    
def quick_sort_rec(arr, l, r):
    if l < r:
        pi = partition(arr, l, r)
        quick_sort_rec(arr, l, pi - 1)
        quick_sort_rec(arr, pi + 1, r)
    
def quick_sort(arr):
    quick_sort_rec (arr, 0, len(arr) - 1)
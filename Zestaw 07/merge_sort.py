def merge_sort_rec(arr, l, r):
    if l < r:
        mid = (l + r) // 2
        merge_sort_rec(arr, l, mid)
        merge_sort_rec(arr, mid + 1, r)
        
        T = [None] * (r - l + 1)
        l1 = l
        r1 = mid
        l2 = mid + 1
        r2 = r
        i = 0
        while l1 <= r1 and l2 <= r2:
            if arr[l1] <= arr[l2]:
                T[i] = arr[l1]
                l1 += 1
            else:
                T[i] = arr[l2]
                l2 += 1
            i += 1
        
        while l1 <= r1:
            T[i] = arr[l1]
            l1 += 1
            i += 1
        while l2 <= r2:
            T[i] = arr[l2]
            l2 += 1
            i += 1
        
        for i in range(r - l +1):
            arr[l + i] = T[i]

def merge_sort (arr):
    merge_sort_rec (arr, 0, len(arr) - 1)
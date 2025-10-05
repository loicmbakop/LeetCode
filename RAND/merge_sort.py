def merge_sorrt(arr):
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left_merge = merge_sorrt(left)
    right_merge = merge_sorrt(right)

    return merge(left_merge, right_merge)

def merge(left, right):
    res = []
    i,j = 0,0
    while i< len(left)and j <len(right):
        if left[i] <= right[j]:
            res.append(left[i])  
            i = i+1
        else:
            res.append(right[j])
            j = j+1
    res.extend(left[i:])
    res.extend(right[j:])
    return res
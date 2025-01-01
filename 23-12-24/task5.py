def reverse_list(arr): 
    ls = []
    for i in range(len(arr)-1, -1, -1):
        ls.append(arr[i])
    return ls

print(reverse_list([1, 2, 3, 4, 5]))
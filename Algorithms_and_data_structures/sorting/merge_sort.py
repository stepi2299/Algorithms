def merge_sort(data):
    if len(data) == 0:
        return data
    if len(data)>1:
        middle = len(data)//2
        left = data[:middle]
        right = data[middle:]
        merge_sort_2(left)
        merge_sort_2(right)
        merge_3_tables(data, left, right)
        return data

def merge_3_tables(data, left, right):
    ll = len(left)
    lr = len(right)
    i = j = k = 0
    while i < ll and j < lr:
        if left[i] < right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        k += 1
    while i < ll:
        data[k] = left[i]
        i += 1
        k += 1
    while j < lr:
        data[k] = right[j]
        k += 1
        j += 1

def merge_sort_2(data):
    data_size = len(data)
    new_data = [None for i in range(data_size)]
    sort(data, new_data, 0, data_size-1)
    return data


def sort(old, new, low, high):
    if high <= low:
        return
    middle = low + (high-low) // 2
    sort(old, new, low, middle)
    sort(old, new, middle+1, high)
    place_merge(old, new, low, middle, high)


def place_merge(old, new, low, middle, high):
    for k in range(high-low+1):
        k += low
        new[k] = old[k]
    i = low
    j = middle+1
    for k in range(high-low+1):
        k += low
        if i > middle:
            old[k] = new[j]
            j += 1
        elif j > high:
            old[k] = new[i]
            i += 1
        elif new[j] < new[i]:
            old[k] = new[j]
            j += 1
        else:
            old[k] = new[i]
            i += 1
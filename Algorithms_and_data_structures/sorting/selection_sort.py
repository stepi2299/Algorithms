def selection_sort(contents):
    for i in range(0, len(contents)):
        min_index = i
        for j in range(i, len(contents)):
            if contents[j] < contents[min_index]:
                min_index = j
        if min_index != i:
            contents[i], contents[min_index] = contents[min_index], contents[i]
    return contents

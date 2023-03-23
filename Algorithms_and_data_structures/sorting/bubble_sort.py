def bubble_sort(data):
    data_len = len(data)
    if data_len == 0:
        return data
    for i in range(data_len):
        for j in range(data_len-i-1):
            if data[j] > data[j+1]:
                tmp = data[j]
                data[j] = data[j+1]
                data[j+1] = tmp
    return data

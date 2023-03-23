import time
from matplotlib import pyplot as plt

from quick_sort import quick_sort
from merge_sort import merge_sort
from bubble_sort import bubble_sort
from selection_sort import selection_sort


def creating_input(file_path):
    text = []
    skips = [".", ",", ":", ";", "'", '"', '!', '?', '—', '(', ')', '…', '«', '»']
    with open(file_path, "r") as file:
        for line in file:
            for ch in skips:
                line = line.replace(ch, "")
            line = line.rstrip()
            for word in line.split(" "):
                if len(word) > 0:
                    text.append(word)
    return text


def creating_data_for_plots(data, processing_func, word_difference=1000, time_bound=10, word_limit=None):
    processing_time = []
    words_number = []
    max_words_number = len(data)
    for i in range(max_words_number//word_difference):
        i += 1
        words_count = int(i*word_difference)
        input_data = data[:words_count]
        st = time.perf_counter()
        out = processing_func(input_data)
        current_time = time.perf_counter()-st
        processing_time.append(current_time)
        words_number.append(words_count)
        if current_time > time_bound:
            break
        if word_limit and i >= word_limit / word_difference:
            break
    return words_number, processing_time


def creating_plots(list_of_x_y):
    plt.xlabel("Number of words")
    plt.ylabel("Processing time in sec")
    plt.title("Plot showing relationship processing time and problem size in sorting")
    for enum_i, plot_args in enumerate(list_of_x_y):
        x, y = plot_args
        sorting_names = ['bubble_sort', 'selection_sort', 'merge_sort', 'quick_sort']
        plt.plot(x, y, label=sorting_names[enum_i])
    plt.legend()
    plt.show()


def catch_data_to_file(list_of_data):
    with open("data_caught.txt", 'w') as fh:
        for from_alg in list_of_data:
            cnt, tm = from_alg
            for a, b in zip(cnt, tm):
                fh.write(f"{a}: {b}\n")


if __name__ == "__main__":
    data = creating_input('sortowanie/pan-tadeusz-unix.txt')
    list_of_data = []
    sorting_algorithms = [bubble_sort, selection_sort, merge_sort, quick_sort]
    for algorithm in sorting_algorithms:
        count, times = creating_data_for_plots(data, algorithm, time_bound=20, word_limit=10000)
        list_of_data.append((count, times))
    catch_data_to_file(list_of_data)
    creating_plots(list_of_data)

from random import choice, randint
from matplotlib import pyplot as plt
import time

from n import find as n_find
from kmp import find as kmp_find
from kr import find as kr_find


def test_algorithms():
    alphabet = ['a', 'b']
    text = ''
    for _ in range(100):
        text += choice(alphabet)
    print(f"Text: {text}")
    pattern = ''
    for _ in range(randint(3, 6)):
        pattern += choice(alphabet)
    print(f"Searching pattern: {pattern}")

    build_in_resultats = []
    find_start = 0
    find_end = len(text)
    while True:
        new_resultat = text.find(pattern, find_start, find_end)
        if new_resultat == -1:
            break
        build_in_resultats.append(new_resultat)
        find_start = new_resultat + 1

    print(f"Build-in find method: {build_in_resultats}")
    print(f"Algorithm N found answer: {n_find(pattern, text)}")
    print(f"Algorithm KMP found answer: {kmp_find(pattern, text)}")
    print(f"Algorithm KR found answer: {kr_find(pattern, text)}")


def compare_algorithms(word_difference, iterations, time_out):
    huge_text = get_pan_tadeusz('pan-tadeusz-unix.txt')
    words_list = get_words_list('pan-tadeusz-unix.txt')
    algorithms_list = [n_find, kmp_find, kr_find]
    plot_data = []
    for algorithm in algorithms_list:
        print('new algorithm')
        alg_times = []
        alg_words = []
        for i in range(1, iterations + 1):
            print('iteration:', i)
            words_to_find = words_list[:i*word_difference]
            start_finding = time.time()
            for word in words_to_find:
                algorithm(word, huge_text)
            stop_finding = time.time()
            finding_total_time = stop_finding - start_finding
            alg_times.append(finding_total_time)
            alg_words.append(i*word_difference)
        plot_data.append((alg_words, alg_times))
    create_plot(plot_data)


def create_plot(data):
    plt.xlabel("Number of words to find")
    plt.ylabel("Processing time in sec")
    plt.title("Plot showing relationship processing time and problem size in searching")
    for enum_i, plot_args in enumerate(data):
        x, y = plot_args
        sorting_names = ['n_find', 'kmp_find', 'kr_find']
        plt.plot(x, y, label=sorting_names[enum_i])
    plt.legend()
    plt.show()


def get_words_list(file_path):
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


def get_pan_tadeusz(file_path):
    pan_tadeusz = ""
    with open(file_path, 'r') as fh:
        for line in fh:
            pan_tadeusz += line
    return pan_tadeusz


if __name__ == "__main__":
    # test_algorithms()
    compare_algorithms(50, 10, 10)

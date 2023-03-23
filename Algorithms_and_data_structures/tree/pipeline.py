import random
import time
from matplotlib import pyplot as plt

from bst import BST
from avl import AVL


def generate_input_list(size, shuffle=True):
    input_list = []
    hist = 1
    for i in range(size):
        input_list.append(hist)
        hist += random.randint(1, 4)
    if shuffle:
        random.shuffle(input_list)
    return input_list


def generate_plot_creating_time(input_list, step_size, step_limit):
    bst_times = []
    avl_times = []
    for i in range(1, step_limit):
        bst_start_time = time.time()
        bst = BST(input_list[0])
        for key in input_list[1:i*step_size - 1]:
            bst.insert(key)
        bst_stop_time = time.time()
        bst_times.append(bst_stop_time - bst_start_time)

        avl_start_time = time.time()
        avl = AVL(input_list[0])
        for key in input_list[1:i*step_size - 1]:
            avl.insert(key)
        avl_stop_time = time.time()
        avl_times.append(avl_stop_time - avl_start_time)
    plt.xlabel("Number of elements")
    plt.ylabel("Processing time in sec")
    plt.title("Tree creation time from increasing key value")
    # increasing key value | random data
    words = [i*step_size for i in range(1, step_limit)]
    plt.plot(words, bst_times, label="BST")
    plt.plot(words, avl_times, label="AVL")
    plt.legend()
    plt.show()


def generate_plot_searching_time(input_list, step_size, step_limit):
    bst_times = []
    avl_times = []

    bst = BST(input_list[0])
    for key in input_list[1:]:
        bst.insert(key)

    avl = AVL(input_list[0])
    for key in input_list[1:]:
        avl.insert(key)

    bst_start_time = time.time()
    for i in range(1, step_limit):
        bst_start_time = time.time()
        for key in input_list[0:i*step_size]:
            bst.get(key)
        bst_stop_time = time.time()
        bst_times.append(bst_stop_time - bst_start_time)

    avl_start_time = time.time()
    for i in range(1, step_limit):
        avl_start_time = time.time()
        for key in input_list[0:i*step_size]:
            avl.get(key)
        avl_stop_time = time.time()
        avl_times.append(avl_stop_time - avl_start_time)

    plt.xlabel("Number of gets")
    plt.ylabel("Processing time in sec")
    plt.title("Time for get operation from random data")
    # increasing key value | random data
    words = [i*step_size for i in range(1, step_limit)]
    plt.plot(words, bst_times, label="BST")
    plt.plot(words, avl_times, label="AVL")
    plt.legend()
    plt.show()


def generate_plot_deleting_time(input_list, step_size, step_limit):
    bst_times = []
    avl_times = []

    bst_start_time = time.time()
    for i in range(1, step_limit):
        bst = BST(input_list[0])
        for key in input_list[1:]:
            bst.insert(key)
        bst_start_time = time.time()
        for key in input_list[0:i*step_size]:
            bst.delete(key)
        bst_stop_time = time.time()
        bst_times.append(bst_stop_time - bst_start_time)

    avl_start_time = time.time()
    for i in range(1, step_limit):
        avl = AVL(input_list[0])
        for key in input_list[1:]:
            avl.insert(key)
        avl_start_time = time.time()
        for key in input_list[0:i*step_size]:
            avl.delete(key)
        avl_stop_time = time.time()
        avl_times.append(avl_stop_time - avl_start_time)

    plt.xlabel("Number of delets")
    plt.ylabel("Processing time in sec")
    plt.title("Time for delete operation increasing key value")
    # increasing key value | random data
    words = [i*step_size for i in range(1, step_limit)]
    plt.plot(words, bst_times, label="BST")
    plt.plot(words, avl_times, label="AVL")
    plt.legend()
    plt.show()


def display_example(size):
    keys = generate_input_list(30)
    bst = BST(keys[0])
    for key in keys[1:]:
        bst.insert(key)
    print("------ BST diplay ------")
    bst.display()
    print("------ end diplay ------")
    avl = AVL(keys[0])
    for key in keys[1:]:
        avl.insert(key)
    print("------ AVL diplay ------")
    avl.display()
    print("------ end diplay ------")


if __name__ == "__main__":
    generated_list = generate_input_list(5000, shuffle=False)
    # generate_plot_creating_time(generated_list, 1000, 11)
    # generate_plot_searching_time(generated_list, 500, 11)
    # generate_plot_deleting_time(generated_list, 500, 11)
    display_example(30)

import random
from heap import Heap
import time
from matplotlib import pyplot as plt


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
    heap_two_times = []
    heap_three_times = []
    heap_four_times = []

    for i in range(1, step_limit):
        heap_two = Heap(2)
        heap_two_start = time.perf_counter()
        heap_two.make_heap(input_list.copy()[0:i*step_size - 1])
        heap_two_stop = time.perf_counter()
        heap_two_times.append(heap_two_stop - heap_two_start)

        heap_three = Heap(3)
        heap_three_start = time.perf_counter()
        heap_three.make_heap(input_list[0:i*step_size - 1])
        heap_three_stop = time.perf_counter()
        heap_three_times.append(heap_three_stop - heap_three_start)

        heap_four = Heap(4)
        heap_four_start = time.perf_counter()
        heap_four.make_heap(input_list[0:i*step_size - 1])
        heap_four_stop = time.perf_counter()
        heap_four_times.append(heap_four_stop - heap_four_start)
    plt.xlabel("Number of elements")
    plt.ylabel("Processing time in sec")
    plt.title("Tree creation time using make heap")
    # increasing key value | random data
    words = [i*step_size for i in range(1, step_limit)]
    plt.plot(words, heap_two_times, label="Heap 2 arms")
    plt.plot(words, heap_three_times, label="Heap 3 arms")
    plt.plot(words, heap_four_times, label="Heap 4 arms")
    plt.legend()
    plt.show()

def generate_plot_creating_time_naive(input_list, step_size, step_limit):
    heap_two_times = []
    heap_three_times = []
    heap_four_times = []

    for i in range(1, step_limit):
        heap_two = Heap(2)
        heap_two_start = time.perf_counter()
        for val in input_list[0: i*step_size - 1]:
            heap_two.push(val)
        heap_two_stop = time.perf_counter()
        heap_two_times.append(heap_two_stop - heap_two_start)

        heap_three = Heap(3)
        heap_three_start = time.perf_counter()
        for val in input_list[0: i * step_size - 1]:
            heap_three.push(val)
        heap_three_stop = time.perf_counter()
        heap_three_times.append(heap_three_stop - heap_three_start)

        heap_four = Heap(4)
        heap_four_start = time.perf_counter()
        for val in input_list[0: i * step_size - 1]:
            heap_four.push(val)
        heap_four_stop = time.perf_counter()
        heap_four_times.append(heap_four_stop - heap_four_start)
    plt.xlabel("Number of elements")
    plt.ylabel("Processing time in sec")
    plt.title("Tree creation time using naive algorithm")
    words = [i*step_size for i in range(1, step_limit)]
    plt.plot(words, heap_two_times, label="Heap 2 arms")
    plt.plot(words, heap_three_times, label="Heap 3 arms")
    plt.plot(words, heap_four_times, label="Heap 4 arms")
    plt.legend()
    plt.show()

def generate_plot_heap_pop(input_list, step_size, step_limit):
    heap_two_times = []
    heap_three_times = []
    heap_four_times = []

    for i in range(1, step_limit):
        heap_two = Heap(2)
        heap_two.make_heap(input_list.copy())
        heap_two_start = time.perf_counter()
        for count in range(step_size*i):
            heap_two.pop()
        heap_two_stop = time.perf_counter()
        heap_two_times.append(heap_two_stop - heap_two_start)

        heap_three = Heap(3)
        heap_three.make_heap(input_list.copy())
        heap_three_start = time.perf_counter()
        for count in range(step_size * i):
            heap_three.pop()
        heap_three_stop = time.perf_counter()
        heap_three_times.append(heap_three_stop - heap_three_start)

        heap_four = Heap(4)
        heap_four.make_heap(input_list.copy())
        heap_four_start = time.perf_counter()
        for count in range(step_size * i):
            heap_four.pop()
        heap_four_stop = time.perf_counter()
        heap_four_times.append(heap_four_stop - heap_four_start)
    plt.xlabel("Number popped elements")
    plt.ylabel("Processing time in sec")
    plt.title("Popping n elements from the tree")
    words = [i*step_size for i in range(1, step_limit)]
    plt.plot(words, heap_two_times, label="Heap 2 arms")
    plt.plot(words, heap_three_times, label="Heap 3 arms")
    plt.plot(words, heap_four_times, label="Heap 4 arms")
    plt.legend()
    plt.show()



def display_example(size):
    values = generate_input_list(size)
    heap_two_arms = Heap(2)
    heap_two_arms.make_heap(values)
    print("------ Heap Two Arms diplay ------")
    heap_two_arms.display()
    heap_three_arms = Heap(3)
    heap_three_arms.make_heap(values)
    print("------ Heap Three Arms diplay ------")
    heap_three_arms.display()
    heap_four_arms = Heap(4)
    heap_four_arms.make_heap(values)
    print("------ Heap Four Arms diplay ------")
    heap_four_arms.display()
    print("------ end diplay ------")

if __name__ == "__main__":
    generated_list = generate_input_list(10000, shuffle=True)
    # generate_plot_creating_time(generated_list, 500, 21)
    # generate_plot_creating_time_naive(generated_list, 500, 200)
    #generate_plot_heap_pop(generated_list, 500, 21)
    display_example(40)


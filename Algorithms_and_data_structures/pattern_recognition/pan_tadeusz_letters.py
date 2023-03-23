def get_alphabet():
    letters = []
    with open("./pan-tadeusz-unix.txt", 'r') as fh:
        for line in fh:
            for letter in line:
                try:
                    letters.index(letter)
                except ValueError:
                    letters.append(letter)
    return letters


def my_test():
    with open("pipeline.py", 'r') as fh:
        print(fh)


if __name__ == "__main__":
    letters_list = get_alphabet()
    alphabet = ''.join(letters_list)
    print(alphabet)

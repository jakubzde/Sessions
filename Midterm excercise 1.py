def print_b_words(file_name):
    """
    Print all the words in the file that start with the letter 'b'.
    :param file_name: the file name
    :return: none
    """
    punctuation = ",.!?\n"
    with open(file_name, "r") as file:
        for line in file:
            for p in punctuation:
                line = line.replace(p, "")
            words = line.split(" ")
            for word in words:
                if (word.startswith('b') or word.startswith('B')) and len(word) == 3:
                    print(word)

print_b_words('midterm_ex_1.txt')
# file = open("file1.txt")
# print(file.read())
# result = [int(num) for num in open("file1.txt") if num in open("file2.txt")]
# print(result)

import pandas

nato_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {value.letter: value.code for (key, value) in nato_dataframe.iterrows()}
print(nato_dict)


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        code_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Use letters in the alphabet only")
        generate_phonetic()
    else:
        print(code_list)


generate_phonetic()

def get_input():
    input("Enter a word: ")

def print_vertical(word):
    for letter in word:
        print(letter)


input_word = get_input()
print("Printing word vertically:")
print_vertical(input_word)


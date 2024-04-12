import sys
import os
import operator


def tokenize(text_file_path: str) -> list:
    """
    Runtime Complexity: This is O(N^2) because it uses 2 for loops. One that reads through
    each line in the text file and another to read through the characters in each line.

    Reads in a text file and returns a list of the tokens in that file.
    For the purposes of this project, a token is a sequence of alphanumeric characters, independent of capitalization

    :param text_file_path: Path to the text file to be read.
    :return: List of the tokens in that file.
    """

    # initialize list of tokens and variables
    list_of_tokens = []
    token = ""
    special_characters = '!\"#$%&\'()*+,-./\\:;<=>?@[]^_`{|}~:\n'

    # opening and reading in a text file
    with open(text_file_path, 'r') as text_file:
        # Reads each line from the file
        for line in text_file:
            # Converts each line to lowercase
            low_case_line: str = line.lower()

            for char in low_case_line:
                # Checks to see if a word has a special character
                if char == " " or char in special_characters:
                    if token:
                        # Checks if it's an actual word
                        if token.isalnum() and token.isascii():
                            list_of_tokens.append(token)
                    word = ""
                else:
                    # Adds character to token to form a word
                    token += char

        # Gets last word in line
        if token:
            if token.isalnum() and token.isascii():
                list_of_tokens.append(token)

    return list_of_tokens


def compute_word_frequencies(tokens: list) -> dict:
    """
    Runtime Complexity: This is O(N) because it uses a for loop to look through each token
    in the list of tokens

    Counts the number of occurrences of each token in the token list.
    Must write this from scratch.

    :param tokens: List of tokens.
    :return: dict, mapping each token to the number of occurrences.
    """
    # Initialize dictionary that indicates number of occurrences
    word_frequencies = {}

    # Looks through list of tokens
    for token in tokens:
        # Checks if token is already in dictionary and increments it by 1
        if token in word_frequencies:
            word_frequencies[token] += 1
        # Sets count to 1 if it isn't
        else:
            word_frequencies[token] = 1

    return word_frequencies


def print_frequencies(frequencies: dict) -> None:
    """
    Runtime Complexity: It is O(nlogn) because of the sorting function used.


    <token>-> <freq>


    Prints out the word frequency count, ordered by decreasing frequency (so, the highest frequency words first).

    :param frequencies: dict, mapping each token to the number of occurrences.
    """
    # Sorts frequency count in descending order
    sorted_freq = sorted(frequencies.items(), key=operator.itemgetter(1), reverse=True)

    for token, freq in sorted_freq:
        print(f"<{token}> -> <{freq}>")


if __name__ == '__main__':
    tokens = tokenize(sys.argv[1])
    freqs = compute_word_frequencies(tokens)
    print_frequencies(freqs)

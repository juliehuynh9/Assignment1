import sys
import os
import operator

def tokenize(text_file_path: str) -> list:
    """
    Runtime Complexity: This function is O(N^2) because we used a for loop within a for loop

    Reads in a text file and returns a list of the tokens in that file.
    For the purposes of this project, a token is a sequence of alphanumeric characters, independent of capitalization.

    :param text_file_path: Path to the text file to be read.
    :return: List of the tokens in that file.
    """

    # Initialize list of tokens
    list_of_tokens = []

    try:
        # Open and read in a text file
        with open(text_file_path, 'r', encoding='utf-8') as text_file:
            # Iterate over each line in the file
            for line in text_file:
                # Split the line into words
                words = line.split()
                # Process each word
                for word in words:
                    # Check if the word contains only alphanumeric characters and is ASCII and join each character
                    token = ''.join(char for char in word if char.isalnum() and char.isascii())
                    if token:
                        # Append the token to the list of tokens in lowercase
                        list_of_tokens.append(token.lower())

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

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
        print(f"{token} -> {freq}")


if __name__ == '__main__':
    tokens = tokenize(sys.argv[1])
    freqs = compute_word_frequencies(tokens)
    print_frequencies(freqs)

import sys
import os
import operator


def tokenize(text_file_path: str) -> list:
    """
    Runtime Complexity: This is O(N^2) because it uses a for loop within a for loop.

    Reads in a text file and returns a list of the tokens in that file.
    For the purposes of this project, a token is a sequence of alphanumeric characters, independent of capitalization.

    :param text_file_path: Path to the text file to be read.
    :return: List of the tokens in that file.
    """

    # Initialize list of tokens
    list_of_tokens = []
    buffer_size = 256
    temp_token = b''

    try:
        # Open and read in a text file byte by byte
        with open(text_file_path, 'rb') as text_file:
            while True:
                # Read one byte
                byte = text_file.read(1)
                if not byte:
                    # Break loop if end of file reached
                    break

                # Check if byte is a newline character
                if byte == b'\n':
                    # Split temp_token into lines
                    lines = temp_token.split(b'\n')
                    temp_token = lines.pop() if lines else b''  # Store the last incomplete line

                    # Process complete lines
                    for line in lines:
                        # Split the line into words
                        words = line.split()
                        for word in words:
                            # Check if word is alphanumeric
                            token = b''.join(bytes([char]) for char in word if chr(char).isalnum() and chr(char).isascii())
                            if token:
                                list_of_tokens.append(token.lower().decode('utf-8'))

                else:
                    # Append byte to temp_token
                    temp_token += byte

        # Process the remaining incomplete line
        if temp_token:
            words = temp_token.split()
            for word in words:
                # Check if word is alphanumeric
                token = b''.join(bytes([char]) for char in word if chr(char).isalnum() and chr(char).isascii())
                if token:
                    list_of_tokens.append(token.lower().decode('utf-8'))

        if not list_of_tokens:
            print("0")

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

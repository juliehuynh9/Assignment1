import PartA as A
import sys

"""
    Runtime Complexity: This is O(N^2) because it uses the tokenize method from Part A which
    was O(N^2).

    Finds the common works from the 2 files tokens.

    :param: 2 text files.
    :return: number of common words and common words itself.
    """


def find_common_words(text_file_1, text_file_2):
    # Getting the tokens in each text file
    file1_tokens = A.tokenize(text_file_1)
    file2_tokens = A.tokenize(text_file_2)

    # Put first file's tokens in dictionary
    file1_words = A.compute_word_frequencies(file1_tokens)

    # Create counter for common words and initialize set so we have no duplicates
    common_words_counter = 0
    common_words = set()

    # Check to see if file2 tokens are in the dictionary for file1
    for token in file2_tokens:
        if token in file1_words and token not in common_words:
            # Update counter and add token
            common_words_counter += 1
            common_words.add(token)

    # printing out the common tokens
    for word in common_words:
        print(word)

    print("Common words: ", common_words_counter)


if __name__ == '__main__':
    text_file_1 = sys.argv[1]
    text_file_2 = sys.argv[2]

    find_common_words(text_file_1, text_file_2)

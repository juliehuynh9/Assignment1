import PartA as A
import sys

# implement common word count function

if __name__ == '__main__':
    text_file_1 = sys.argv[1]
    text_file_2 = sys.argv[2]

    file1_tokens = A.tokenize(text_file_1)
    file2_tokens = A.tokenize(text_file_2)
import os
import logging

# Configure module-level logger
logger = logging.getLogger(__name__)

# -----------------------------
# Original Functions (refined)
# -----------------------------

def count_lines(filepath):
    """Counts the number of lines in a given text file.

    Raises FileNotFoundError if the file does not exist.
    """
    with open(filepath, 'r', encoding='utf-8', newline='') as f:
        return sum(1 for _ in f)


def reverse_lines(input_filepath, output_filepath):
    """Reads lines from input_filepath, reverses each, and writes to output_filepath.

    Preserves original line endings (LF, CRLF, CR) and does not add/remove trailing
    newline if the last line had none.

    Raises:
        FileNotFoundError: If the input file does not exist.
        ValueError: If input and output paths are the same.
    """
    if os.path.abspath(input_filepath) == os.path.abspath(output_filepath):
        raise ValueError('input_filepath and output_filepath must differ')

    with open(input_filepath, 'r', encoding='utf-8', newline='') as infile, \
         open(output_filepath, 'w', encoding='utf-8', newline='') as outfile:
        for line in infile:
            eol = ''
            if line.endswith('\r\n'):
                eol = '\r\n'
                content = line[:-2]
            elif line.endswith('\n'):
                eol = '\n'
                content = line[:-1]
            elif line.endswith('\r'):
                eol = '\r'
                content = line[:-1]
            else:
                content = line
            outfile.write(content[::-1] + eol)

    logger.debug("Reversed lines from '%s' to '%s'", input_filepath, output_filepath)


# -----------------------------
# New Functions for PR (refined)
# -----------------------------

def count_words(filepath):
    """Counts the total number of words in a text file.

    A word is defined by whitespace separation.

    Raises FileNotFoundError if the file does not exist.
    """
    with open(filepath, 'r', encoding='utf-8', newline='') as f:
        return sum(len(line.split()) for line in f)


def uppercase_lines(input_filepath, output_filepath):
    """Reads lines from input file, converts to uppercase, writes to output file.

    Preserves original line endings (LF, CRLF, CR).

    Raises:
        FileNotFoundError: If the input file does not exist.
        ValueError: If input and output paths are the same.
    """
    if os.path.abspath(input_filepath) == os.path.abspath(output_filepath):
        raise ValueError('input_filepath and output_filepath must differ')

    with open(input_filepath, 'r', encoding='utf-8', newline='') as fin, \
         open(output_filepath, 'w', encoding='utf-8', newline='') as fout:
        for line in fin:
            eol = ''
            if line.endswith('\r\n'):
                eol = '\r\n'
                content = line[:-2]
            elif line.endswith('\n'):
                eol = '\n'
                content = line[:-1]
            elif line.endswith('\r'):
                eol = '\r'
                content = line[:-1]
            else:
                content = line
            fout.write(content.upper() + eol)

    logger.debug("Converted lines to uppercase from '%s' to '%s'", input_filepath, output_filepath)


def sum_of_digits(n):
    """Returns the sum of decimal digits of integer n."""
    return sum(int(d) for d in str(abs(n)))

# TODO: Add integration tests for end-to-end application behavior


# -----------------------------
# Example Usage
# -----------------------------
if __name__ == "__main__":
    # Basic logging configuration for demo purposes
    logging.basicConfig(level=logging.INFO)

    test_file = "sample.txt"
    reversed_file = "reversed_sample.txt"
    uppercase_file = "uppercase_sample.txt"

    # Create a sample file for testing
    with open(test_file, 'w', encoding='utf-8', newline='') as f:
        f.write("Hello World\n")
        f.write("Python is fun\r\n")
        f.write("Master Thesis")  # no trailing newline

    try:
        line_count = count_lines(test_file)
        print(f"Lines in '{test_file}': {line_count}")
        word_count = count_words(test_file)
        print(f"Words in '{test_file}': {word_count}")
        reverse_lines(test_file, reversed_file)
        uppercase_lines(test_file, uppercase_file)
        print("Processing complete.")
    except Exception as e:
        print(f"Error during processing: {e}")

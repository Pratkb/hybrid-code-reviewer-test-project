import logging
import os

# -----------------------------
# Utility / Library Functions
# -----------------------------

logger = logging.getLogger(__name__)


def count_lines(filepath: str) -> int:
    """Counts the number of lines in a given text file in a memory-efficient manner.

    Raises:
        FileNotFoundError: If the file does not exist.
        OSError: If the file cannot be opened.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)


def reverse_lines(input_filepath: str, output_filepath: str) -> None:
    """Reads lines from input_filepath, reverses the content of each line, and writes to output_filepath.

    Preserves original end-of-line (EOL) characters per line and streams data to avoid high memory usage.

    Raises:
        ValueError: If input and output file paths are the same.
        FileNotFoundError: If the input file does not exist.
        OSError: If an I/O error occurs.
    """
    if os.path.abspath(input_filepath) == os.path.abspath(output_filepath):
        raise ValueError('input_filepath and output_filepath must differ')

    # Use newline='' to avoid automatic newline translation so we can preserve EOLs.
    with open(input_filepath, 'r', encoding='utf-8', newline='') as infile, \
         open(output_filepath, 'w', encoding='utf-8', newline='') as outfile:
        for line in infile:
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
                eol = ''
                content = line
            outfile.write(content[::-1] + eol)


def count_words(filepath: str) -> int:
    """Counts the total number of words in a text file in a streaming fashion.

    Words are split on whitespace using str.split().

    Raises:
        FileNotFoundError: If the file does not exist.
        OSError: If the file cannot be opened.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return sum(len(line.split()) for line in f)


def uppercase_lines(input_filepath: str, output_filepath: str) -> None:
    """Converts all lines from input file to uppercase and writes them to output file.

    Streams line-by-line and preserves existing EOL characters.

    Raises:
        ValueError: If input and output file paths are the same.
        FileNotFoundError: If the input file does not exist.
        OSError: If an I/O error occurs.
    """
    if os.path.abspath(input_filepath) == os.path.abspath(output_filepath):
        raise ValueError('input_filepath and output_filepath must differ')

    with open(input_filepath, 'r', encoding='utf-8', newline='') as fin, \
         open(output_filepath, 'w', encoding='utf-8', newline='') as fout:
        for line in fin:
            fout.write(line.upper())


def sum_of_digits(n: int) -> int:
    """Return the sum of the digits of an integer n."""
    return sum(int(d) for d in str(abs(n)))

# TODO: Add integration tests for end-to-end application behavior.


# -----------------------------
# Example Usage
# -----------------------------
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    test_file = "sample.txt"
    reversed_file = "reversed_sample.txt"
    uppercase_file = "uppercase_sample.txt"

    try:
        # Create a sample file for testing
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write("Hello World\n")
            f.write("Python is fun\n")
            f.write("Master Thesis")  # Intentionally no trailing newline on last line

        print(f"Lines in '{test_file}': {count_lines(test_file)}")
        print(f"Words in '{test_file}': {count_words(test_file)}")

        reverse_lines(test_file, reversed_file)
        uppercase_lines(test_file, uppercase_file)

        print("Processing complete.")
    except Exception:
        logger.exception("An error occurred during example usage")

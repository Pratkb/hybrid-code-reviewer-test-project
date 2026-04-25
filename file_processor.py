import os
import logging

# -----------------------------
# Logger setup
# -----------------------------
logger = logging.getLogger(__name__)

# -----------------------------
# Original Functions (refined)
# -----------------------------

def count_lines(filepath: str) -> int:
    """Count the number of lines in a given text file.

    Returns:
        int: The number of lines.

    Raises:
        FileNotFoundError: If the file does not exist.
        OSError: For other I/O related errors.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)


def reverse_lines(input_filepath: str, output_filepath: str) -> None:
    """Read lines from input_filepath, reverse each line's content while preserving
    the original line endings (EOLs), and write to output_filepath.

    Preserves per-line EOLs including \"\r\n\", \"\n\", and \"\r\". Processes the file in a streaming manner
    to minimize memory usage.

    Raises:
        ValueError: If input_filepath and output_filepath refer to the same file.
        FileNotFoundError: If the input file does not exist.
        OSError: For other I/O related errors.
    """
    if os.path.abspath(input_filepath) == os.path.abspath(output_filepath):
        raise ValueError("input_filepath and output_filepath must differ")

    # Use newline='' to preserve original line endings
    with open(input_filepath, 'r', encoding='utf-8', newline='') as infile, \
         open(output_filepath, 'w', encoding='utf-8', newline='') as outfile:
        for line in infile:
            # Detect EOL
            if line.endswith("\r\n"):
                eol = "\r\n"
                content = line[:-2]
            elif line.endswith("\n"):
                eol = "\n"
                content = line[:-1]
            elif line.endswith("\r"):
                eol = "\r"
                content = line[:-1]
            else:
                eol = ""
                content = line
            outfile.write(content[::-1] + eol)


# -----------------------------
# New Functions for PR (refined)
# -----------------------------

def count_words(filepath: str) -> int:
    """Count the total number of words in a text file.

    Returns:
        int: The total number of whitespace-delimited words in the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        OSError: For other I/O related errors.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return sum(len(line.split()) for line in f)


def uppercase_lines(input_filepath: str, output_filepath: str) -> None:
    """Read lines from input file, convert to uppercase, and write to output file.

    Processes the file in a streaming manner and preserves existing line endings
    by using newline='' on both read and write.

    Raises:
        ValueError: If input_filepath and output_filepath refer to the same file.
        FileNotFoundError: If the input file does not exist.
        OSError: For other I/O related errors.
    """
    if os.path.abspath(input_filepath) == os.path.abspath(output_filepath):
        raise ValueError("input_filepath and output_filepath must differ")

    with open(input_filepath, 'r', encoding='utf-8', newline='') as fin, \
         open(output_filepath, 'w', encoding='utf-8', newline='') as fout:
        for line in fin:
            fout.write(line.upper())


# -----------------------------
# Example Usage
# -----------------------------
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    test_file = "sample.txt"
    reversed_file = "reversed_sample.txt"
    uppercase_file = "uppercase_sample.txt"

    # Create a sample file for testing
    with open(test_file, 'w', encoding='utf-8', newline='') as f:
        f.write("Hello World\n")
        f.write("Python is fun\r\n")
        f.write("Master Thesis")

    try:
        print(f"Lines in '{test_file}': {count_lines(test_file)}")
        print(f"Words in '{test_file}': {count_words(test_file)}")
        reverse_lines(test_file, reversed_file)
        uppercase_lines(test_file, uppercase_file)
        print(f"Successfully reversed lines to '{reversed_file}'")
        print(f"Successfully uppercased lines to '{uppercase_file}'")
    except Exception as e:
        logger.error(f"An error occurred during processing: {e}")

import pandas as pd
import numpy as np

# -----------------------------
# Original Functions
# -----------------------------

# function to count lines
def count_lines(filepath):
    """Counts the number of lines in a given text file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return -1
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return -1

# function to reverse lines
def reverse_lines(input_filepath, output_filepath):
    """Reads lines from input_filepath, reverses each, and writes to output_filepath."""
    try:
        with open(input_filepath, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
        
        reversed_lines = [line.rstrip("\r\n")[::-1] + '\n' for line in lines]  # Preserve whitespace
        
        with open(output_filepath, 'w', encoding='utf-8') as outfile:
            outfile.writelines(reversed_lines)
        
        print(f"Successfully reversed lines from '{input_filepath}' to '{output_filepath}'")
        return True
    except FileNotFoundError:
        print(f"Error: Input file not found at {input_filepath}")
        return False
    except Exception as e:
        print(f"An error occurred during reversal: {e}")
        return False

# -----------------------------
# New Functions for PR
# -----------------------------

def count_words(filepath):
    """Counts the total number of words in a text file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return sum(len(line.split()) for line in f)
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return -1
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return -1

def uppercase_lines(input_filepath, output_filepath):
    """Reads lines from input file, converts to uppercase, writes to output file."""
    try:
        with open(input_filepath, 'r', encoding='utf-8') as fin:
            lines = fin.readlines()

        with open(output_filepath, 'w', encoding='utf-8') as fout:
            fout.writelines(line.upper() for line in lines)

        print(f"Successfully converted lines to uppercase from '{input_filepath}' to '{output_filepath}'")
        return True
    except FileNotFoundError:
        print(f"Error: Input file not found at {input_filepath}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def sum_of_digits(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

# -----------------------------
# Example Usage
# -----------------------------
if __name__ == "__main__":
    test_file = "sample.txt"
    reversed_file = "reversed_sample.txt"
    uppercase_file = "uppercase_sample.txt"

    # Create a sample file for testing
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write("Hello World\n")
        f.write("Python is fun\n")
        f.write("Master Thesis\n")

    print(f"Lines in '{test_file}': {count_lines(test_file)}")
    print(f"Words in '{test_file}': {count_words(test_file)}")
    reverse_lines(test_file, reversed_file)
    uppercase_lines(test_file, uppercase_file)

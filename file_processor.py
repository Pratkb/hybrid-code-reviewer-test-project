import pandas as pd
import numpy as np



def count_lines(filepath):
    """Counts the number of lines in a given text file."""
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return -1
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return -1

def reverse_lines(input_filepath, output_filepath):
    """Reads lines from input_filepath, reverses each, and writes to output_filepath."""
    try:
        with open(input_filepath, 'r') as infile:
            lines = infile.readlines()
        
        reversed_lines = [line.strip()[::-1] + '\n' for line in lines] # Simple reversal
        
        with open(output_filepath, 'w') as outfile:
            outfile.writelines(reversed_lines)
        print(f"Successfully reversed lines from '{input_filepath}' to '{output_filepath}'")
        return True
    except FileNotFoundError:
        print(f"Error: Input file not found at {input_filepath}")
        return False
    except Exception as e:
        print(f"An error occurred during reversal: {e}")
        return False

if __name__ == "__main__":
    # Example usage
    test_file = "sample.txt"
    output_file = "reversed_sample.txt"

    # Create a sample file for testing
    with open(test_file, 'w') as f:
        f.write("Hello World\n")
        f.write("Python is fun\n")
        f.write("Master Thesis\n")

    print(f"Lines in '{test_file}': {count_lines(test_file)}")
    reverse_lines(test_file, output_file)
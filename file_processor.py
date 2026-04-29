"""File processing utilities."""

import os
import logging
from typing import Optional

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def count_lines(filepath: str) -> Optional[int]:
    """Counts the number of lines in a given text file.

    Returns the line count on success, or None on failure.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return sum(1 for _ in f)
    except FileNotFoundError:
        logger.error("File not found: %s", filepath)
    except (OSError, UnicodeError) as e:
        logger.error("Failed to count lines for %s: %s", filepath, e)
    return None


def reverse_lines(input_filepath: str, output_filepath: str) -> bool:
    """Reads lines from input_filepath, reverses each, and writes to output_filepath.

    Returns True on success, False on recoverable errors.
    Raises ValueError if input and output paths are the same.
    """
    if os.path.abspath(input_filepath) == os.path.abspath(output_filepath):
        raise ValueError("input_filepath and output_filepath must be different")

    try:
        with open(input_filepath, 'r', encoding='utf-8') as infile, \
             open(output_filepath, 'w', encoding='utf-8') as outfile:
            for line in infile:
                text = line.rstrip('\n')
                outfile.write(text[::-1] + '\n')
        return True
    except FileNotFoundError:
        logger.error("File not found: %s", input_filepath)
    except (OSError, UnicodeError) as e:
        logger.error("Error reversing lines from %s to %s: %s", input_filepath, output_filepath, e)
    return False

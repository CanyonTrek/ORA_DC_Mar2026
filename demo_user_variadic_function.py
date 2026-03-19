#! /usr/bin/env python3
# COMMENTS for DEVELOPERS/CODERS
# Author: DCameron
# Description: This script will demo HOWTO define a VARIADIC function
# which is a function that accepts variable number of parameters!
"""
    This module has several functions for searching for
    Regex patterns in one or more file/s
"""
import re
import sys

# Example of a VARIADIC function which unpacks
# all remaining parameters into a TUPLE
def search_pattern(pattern=r"^.{19}$", *files):
    """ Search for Regex patterns in file/s and return num
        lines matched
    """
    lines = 0
    for file in files:
        try:
            fh_words = open(file, mode="rt")
        except FileNotFoundError as err:
            print(f"Error code {err.args[0]}, msg={err.args[1]}, {err.filename}", file=sys.stderr)
            sys.exit(1)
        except PermissionError as err:
            print(f"Error, {err.args}, {err.filename}", file=sys.stderr)
            sys.exit(2)
        except Exception as err:
            print("Some other error occurred. Investigate", file=sys.stderr)
            sys.exit(3)
        else:
            # Execute if try block succeeds
            for line in fh_words:
                m = re.search(pattern, line)  # Match pattern
                if m:
                    lines += 1
                    print(line, end="")
            fh_words.close() # Close file handle
        finally:
            # Always executes
            print("And now for something completely different")

    return lines

def main():
    num_lines = search_pattern(r"^([A-Z]).*\1$", r"f:\labs\words", r"f:\labs\words2", r"F:\labs\words3")
    print(f"Matched {num_lines} lines")
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)

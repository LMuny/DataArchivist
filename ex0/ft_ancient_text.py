#!/usr/bin/env python
import sys
from typing import IO
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        filename = sys.argv[1]
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{filename}'")
        try:
            f: IO[str] = open(filename, "r")
            content = str = f.read()
            print("---")
            print(content, end="")
            print("---")
            f.close()
            print(f"File '{filename}'closed.")
        except Exception as e:

            print(f"Error opening file '{filename}': {e}")

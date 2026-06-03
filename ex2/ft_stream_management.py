import sys
from typing import IO
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        filename = sys.argv[1]
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{filename}'")
        try:
            f: IO[str] = open(filename, "r")
            content: str = f.read()
            print("---\n")
            print(content, end="")
            print("\n---")
            f.close()
            print(f"File '{filename} 'closed.\n")
            lines: list[str] = content.split("\n")
            new_lines: list[str] = []
            for line in lines:
                if line != "":
                    new_lines.append(line + "#")
            new_content: str = "\n".join(new_lines)
            print("Transform Data:\n---\n")
            print(new_content)
            print("\n---")
            sys.stdout.write("Enter new file name (or empty):")
            sys.stdout.flush()
            new_file: str = sys.stdin.readline().strip()
            if new_file == "":
                print("Not saving data.")
            else:
                print(f"Saving data to '{new_file}'.")
                try:
                    f2: IO[str] = open(new_file, "w")
                    f2.write(new_content + "\n")
                    f2.close()
                    print(f"Data saved in file '{new_file}'")
                except Exception as e:
                    sys.stderr.write(f"[STDERR] Error opening"
                                     f" file '{filename}': {e}")
                    sys.stderr.write("Data not saved.")
        except Exception as e:

            sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}")

def count_lines(file_path: str) -> int:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return sum(1 for _ in file)
    except FileNotFoundError:
        return -1
    except Exception:
        return -2

if __name__ == "__main__":
    file_path = input("Enter the path to your text file: ")
    result = count_lines(file_path)
    if result >= 0:
        print(f"Number of lines: {result}")
    elif result == -1:
        print("File not found")
    else:
        print("An error occurred while reading the file")

def count_lines_and_words(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
        return num_lines, num_words
    except FileNotFoundError:
        return "File not found."

lines, words = count_lines_and_words('./example.txt')
print(f"Number of lines: {lines}")
print(f"Number of words: {words}")
import sys
from stats import count_words
from stats import char_count
from stats import sorted_char_count

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if sys.argv and len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]

    text = get_book_text(filepath)
    num_words = count_words(text)
    num_chars = char_count(text)
    num_chars = sorted_char_count(num_chars)
    print_report(filepath, num_words, num_chars)

def print_report(filepath, num_words, num_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for key, value in num_chars.items():
        if key.isalpha():
            print(key + ":", value)
    print("============= END ===============")

main()
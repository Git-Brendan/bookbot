filepath = "books/frankenstein.txt"

def get_book_text():
    with open(filepath) as f:
        file_contents = f.read()
        print(file_contents)

def main():
    return get_book_text()

main()
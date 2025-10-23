import sys
from stats import get_word_count, get_char_count, sort_char_dict

if not len(sys.argv) == 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

file_name, book_path = sys.argv

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    #book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    book_wc = get_word_count(book_text)
    book_char_count = get_char_count(book_text)
    book_char_sort = sort_char_dict(book_char_count)
    print_report(book_path, book_wc, book_char_sort)


def print_report(book_path, book_wc, book_char_sort):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_wc} total words")
    print("--------- Character Count -------")
    for item in book_char_sort:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()
from stats import get_word_count
from stats import get_char_count
from stats import sort_dict
import sys

def get_book_text(file_path):
    with open(file_path) as file:
        file_contents =  file.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    contents =  get_book_text(file_path)
    
    num_words = get_word_count(contents)
    char_count = get_char_count(contents)
    sorted_chars = sort_dict(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at /books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("-------- Character Count -------")
    for char in sorted_chars:
        if char["character"].isalpha():
            print(f"{char['character']}: {char['count']}")
    print("============= END ===============")


main()
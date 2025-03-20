import os
import sys
from stats import get_book_test, get_word_count, count_chars, get_sorted_chars

if(len(sys.argv) < 2):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    content = get_book_test(sys.argv[1])
    words_count = get_word_count(content)
    print(f"Found {words_count} total words")
    chars_dict = count_chars(content)
    print("----------- Character Count ----------")
    chars_list = get_sorted_chars(chars_dict)
    for item in chars_list:
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

main()
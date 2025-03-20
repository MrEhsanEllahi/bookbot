import os
def get_book_test(path):
    try:
        with open(path) as f:
            file_content = f.read()
    except FileNotFoundError:
        print(f"Error: The file '{path}' does not exist.")
        return None
    return file_content

def get_word_count(content):
    return len(content.split())

def count_chars(string):
    chars_dict = {}
    for char in string:
        lower_char = char.lower()
        if lower_char in chars_dict:
            chars_dict[lower_char] += 1
        else:
            chars_dict[lower_char] = 1
    return chars_dict
def sort_on(item):
    return item["count"]

def get_sorted_chars(chars_dict):
    sorted_list = []
    for char in chars_dict:
        count = chars_dict[char]
        sorted_list.append({"char": char, "count": count})
        sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
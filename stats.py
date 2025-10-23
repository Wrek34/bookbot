#get word count from book
def get_word_count(book_text_string):
    words_split = book_text_string.split()
    num_words = len(words_split)
    return num_words

#get character count from book
def get_char_count(book_text_string):
    char_count = {}
    for char in book_text_string:
        lower_char = char.lower()
        if lower_char in char_count:
            char_count[lower_char] += 1
        else:
            char_count[lower_char] = 1
    return char_count

#helper to sort dictionary
def sort_on(items):
    return items["num"]

#sorts dictionary of charater count by most frequent
def sort_char_dict(char_count):
    char_dict_list = []

    for item in char_count:
        char_dict_list.append({"char": item, "num": char_count[item]})
    char_dict_list.sort(reverse=True, key=sort_on)

    return char_dict_list


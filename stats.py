def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    lower_case_text = text.lower()
    chars = list(lower_case_text)
    char_count = {}
    for char in chars:
        if char in char_count:
            char_count[char] = char_count[char] + 1
        else: 
            char_count[char] = 1
    return char_count

def sort_dict(dictionary):
    sorted_dictionary = []
    for key, val in dictionary.items():
        dict_item = {"character": key, "count": val}
        sorted_dictionary.append(dict_item)
        
    sorted_dictionary.sort(reverse=True, key=sort_on)
    return sorted_dictionary


def sort_on(item):
    return item["count"]

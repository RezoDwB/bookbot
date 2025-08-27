def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(items):
    return items["num"]

def chars_dict_to_sorted_list(char_dict):
    sorted_list = []
    for char, num in char_dict.items():
        char_dict_entry = {"char": char, "num": num}
        sorted_list.append(char_dict_entry)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

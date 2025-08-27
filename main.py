from stats import get_num_words, get_chars_dict, chars_dict_to_sorted_list

def get_book_text(fPath):
    with open(fPath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_list = chars_dict_to_sorted_list(chars_dict)
    #print(num_words,"words found in the document")
    #print(chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for items in sorted_list:
        if items["char"].isalpha():
            print(f"{items['char']}: {items['num']}")

    print("============= END ===============")

main()
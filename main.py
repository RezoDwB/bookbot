from stats import count, letters

def get_book_text(fPath):
    with open(fPath) as f:
        file_contents = f.read()
    return file_contents

def main():
    contents = get_book_text("books/frankenstein.txt")
    num_words = count(contents)
    letter_count = letters(contents)
    print(num_words,"words found in the document")
    print(letter_count)

main()
from stats import get_num_words
from stats import count_chars
def get_book_text(path):
    with open(path) as f:
       text = f.read()
    return text


def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    chars = count_chars(text.lower()) 
    print(f"{num_words} words found in the document")
    print(chars)

main()

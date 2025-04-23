from stats import get_num_words, count_chars, sort_dict
import sys

def get_book_text(path):
    with open(path) as f:
       text = f.read()
    return text


def check_usage():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def main():

    print("============ BOOKBOT ============")
    text = get_book_text(path_to_book)
    print(f"Analyzing book found at {path_to_book}") 
    
    print("----------- Word Count ----------")
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")
    char_count = count_chars(text.lower()) 
    for i in sort_dict(char_count):
        char = i["char"]
        if char.isalpha():
            print(f"{char}: {i['num']}")    
    print("============= END ===============")

check_usage()
path_to_book = sys.argv[1]
main()

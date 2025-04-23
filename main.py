from stats import get_num_words, count_chars, sort_dict


def get_book_text(path):
    with open(path) as f:
       text = f.read()
    return text


def main():
    print("============ BOOKBOT ============")
    text = get_book_text("books/frankenstein.txt")
    print("Analyzing book found at books/frankenstein.txt") 
    
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
main()

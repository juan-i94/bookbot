def get_num_words(text):
    num_words = len(text.split())
    return num_words


def count_chars(text):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# end of file

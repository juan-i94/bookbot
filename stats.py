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

def sort_dict(char_count):
   dict_list = []
   for char, count in char_count.items():
       temporary_dict = {'char': char, 'num': count}
       dict_list.append(temporary_dict)
   # Now we need to sort the list
   def sort_on(dict):
       return dict["num"]

   dict_list.sort(reverse=True, key=sort_on)
   return dict_list


# end of file

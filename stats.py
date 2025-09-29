def get_num_words(the_words):
    num_words = len(the_words.split())  # split into words, count them
    return num_words

def times_each_char(the_words):
    counts = {}
    the_words = the_words.lower()  # make all lowercase
    for char in the_words:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sorted_list(counts):
    new_list = []
    for char, num in counts.items():
        new_list.append({"char": char, "num": num})
    new_list.sort(reverse=True, key=sort_on)
    return new_list

def sort_on(item):
    return item["num"]
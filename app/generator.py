'''This is a for fun only modification of this https://gist.github.com/mattseymour/9205591.

Do not take seriously!!!
'''
import string
import random

def gen():
    all_possible_chars_i_need = string.ascii_letters + string.punctuation + string.digits
    things_i_dont_want = ['\\', '""', '\'', ' ']
    random_string = ''

    lst = [char for char in all_possible_chars_i_need if char not in things_i_dont_want]
    random.shuffle(lst)

    for i in range(0,17):
        position = random.randint(0, len(lst) - 1)

        random_string += lst[position]

    return random_string

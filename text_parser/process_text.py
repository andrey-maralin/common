# coding=UTF-8

import re
import sys
import random


def check_text_validity(text):
    open_bracers = len(re.findall('\[', text))
    close_bracers = len(re.findall('\]', text))
    return open_bracers == close_bracers


def get_option(option_group):
    options = option_group[1:-1].split("|")
    return options[random.randint(0,len(options)-1)]


def find_groups(text):
    rx = r'(\[[^\[$\]\]]*\])'
    return re.findall(rx, text)


def get_result(text):
    found_groups = find_groups(text)
    if check_text_validity(text):
        if found_groups:
            for g in found_groups:
                text = text.replace(g, get_option(g))
            get_result(text)
        else:
            print text
    else:
        print 'Проверьте правильность расстановки [ и ] в введенном тексте.'

if __name__ == "__main__":
    text = sys.argv[1]
    get_result(text)

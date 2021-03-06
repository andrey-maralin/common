# coding=UTF-8

import re
import sys
import random


def is_valid_text(text):
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
    if found_groups:
        for g in found_groups:
            text = text.replace(g, get_option(g))
        get_result(text)
    else:
        print text


if __name__ == "__main__":
    args = sys.argv[1]
    if len(args) < 2:
        print 'Вы забыли ввести текс.'

    text = sys.argv[1].decode("cp1251")

    if is_valid_text(text):
        get_result(text)
    else:
        print 'Проверьте правильность расстановки [ и ] в введенном тексте.'

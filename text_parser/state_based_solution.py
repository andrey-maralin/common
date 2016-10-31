# coding=UTF-8
import random

class WrongBracersOrder(Exception):
    pass


class OptionTree:
    def __init__(self, option_level=0, option_position=0):
        self.option_level = option_level
        self.option_position = option_position
        self.tree = {0: []}

    def add_option_level(self):
        self.tree[self.option_level] = []

    def get_level_len(self, level):
        return self.tree[level]

    def append_option(self, text):
        self.tree[self.option_level].append(text)

    def update_option(self, text):
        self.tree[self.option_level][self.option_position] += text



class Search:
    def __init__(self, text):
        self.initial_text = text
        self.option_tree = OptionTree()
        self.search = {
            'text': iter(text),
            'result': str(),
            'state': 'start',
            'current_option_level': 0
        }

        self.state = {
            'start': self.start,
            'search_for_options': self.search_for_options,
            'search_for_option': self.search_for_option,
            'stop_search': self.stop_search
        }

    def start(self):
        print "Start"
        self.search['state'] = ''

    def stop_search(self):
        print 'Stopping search'
        self.search['state'] = None

    def search_for_options(self):
        print 'Searching for possible options'
        letter = next(self.search['text'])

        if letter == '[':
            self.search['state'] = 'search_for_option'
        elif letter == ']':
            raise WrongBracersOrder
        else:
            self.search['result'] += letter

        # todo put logic here
        self.search['state'] = 'stop_search'

    def search_for_option(self):
        print 'Searching for option'
        letter = next(self.search['text'])

        if letter == '|':
            """
                считаем что если мы наткнулись на '|', значит это новая выриант
            """
            self.option_tree.option_position += 1

        elif letter == '[':
            """
                считаем что если мы наткнулись на '[', значит это вложенный вариант с новым уровнем
            """
            self.option_tree.option_position = 0
            self.option_tree.option_level += 1
            self.option_tree.add_option_level()

        elif letter == ']':

            if self.option_tree.option_level == 0:
                """
                    считаем что если мы наткнулись на ']' и при этом текущий уровень вложенности 0, значит мы подошли
                    к концу вариантов и переходим в новое состояние
                """
                self.option_tree.option_position = 0
                # todo call method which choose between options and put them into result string
                self.search['state'] = 'search_for_options'
            else:
                """
                    в противном случае считаем что закончился вложенный уровень вариантов, поэтому уменьшаем текущий
                     уровень и устанавливание текущую позицию слова в нужное значение
                """
                self.option_tree.option_level -= 1
                self.option_tree.option_position = self.option_tree.get_level_len(self.option_tree.option_level) + 1
        else:
            """
                Если же letter не спец символ, то просто добавляем его в дерево опций с нужным уровнем и позицией
            """
            self.option_tree.update_option(letter)
            # todo put logic here

    def run_search(self):
        while self.search['state'] is not None:
            f = self.state[self.search['state']]
            f()

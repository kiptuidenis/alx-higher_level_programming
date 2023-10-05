#!/usr/bin/python3

import hidden_4


def print_names(module):
    names = dir(module)
    filterd_names = sorted(name for name in names if not name.startswith('__'))
    for name in filterd_names:
        print(name)


if __name__ == '__main__':
    print_names(hidden_4)

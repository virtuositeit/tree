#!/usr/bin/env python3
import subprocess
import sys
import os


def clean_hidden(list):
    newlist = [item for item in list if item[0] != '.']
    return newlist


def sort_name(s):
    if not s[0].isalpha():
        for i in range(len(s)):
            if s[i].isalpha():
                return s[i:].lower()
    else:
        return s.lower()


def walk(path, indent, dash, count):
    files = os.listdir(path)
    files = clean_hidden(files)
    files = sorted(files, key=sort_name)
    for file in files:
        newfile = path + '/' + file
        if file == files[len(files) - 1]:
            if os.path.isdir(newfile):
                count['dir'] += 1
                print(indent + '└── ' + file)
                walk(newfile, indent + '    ', dash, count)
            else:
                count['file'] += 1
                print(indent + '└── ' + file)
        else:
            if os.path.isdir(newfile):
                count['dir'] += 1
                print(indent + '├── ' + file)
                walk(newfile, indent + '│   ', '├── ', count)
            else:
                count['file'] += 1
                print(indent + '├── ' + file)


if __name__ == '__main__':
    path = '.' if len(sys.argv) == 1 or sys.argv[1] == '.' else sys.argv[1]
    print(path)
    i = 0
    count = {'dir': 0, 'file': 0}
    walk(path, '', '', count)
    print()
    print(count['dir'], 'directories,', count['file'], 'files')

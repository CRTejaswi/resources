#!/usr/bin/env python3
import os
import re
import sys
import string
import operator

stack = []
heap = {}


def read_file():
    '''
    POPs a filepath and PUSHes its contents in place.
    '''
    with open(stack.pop()) as f:
        stack.append([f.read()])


def filter_characters():
    '''
    POPs entries from stack and replaces them with a version in which non-alphanumeric characters are replaced by whitespace.
    '''
    stack.append(re.compile('[\W_]+'))
    stack.append([stack.pop().sub(' ', stack.pop()[0]).lower()])


def scan():
    '''
    POPs a string, PUSHes words from the string in place.
    '''
    stack.extend(stack.pop()[0].split())


def remove_stopwords():
    '''
    POPs a list of words from stack, removes stopwords.
    '''
    with open('stopwords.txt') as f:
        stack.append(f.read().split(','))
    stack[-1].extend(list(string.ascii_lowercase))
    heap['words'] = []
    heap['stopwords'] = stack.pop()
    while len(stack) > 0:
        if stack[-1] in heap['stopwords']:
            stack.pop()
        else:
            heap['words'].append(stack.pop())
    stack.extend(heap['words'])
    del heap['words']
    del heap['stopwords']


def frequencies():
    '''
    Takes a list of words and returns dictionary mapping these words with their occurence frequencies.
    '''
    heap['word_frequencies'] = {}
    while len(stack) > 0:
        if stack[-1] in heap['word_frequencies']:
            stack.append(heap['word_frequencies'][stack[-1]])
            stack.append(1)
            stack.append(stack.pop() + stack.pop())
        else:
            stack.append(1)
        heap['word_frequencies'][stack.pop()] = stack.pop()
    stack.append(heap['word_frequencies'])
    del heap['word_frequencies']


def sort():
    stack.extend(sorted(stack.pop().items(), key=operator.itemgetter(1)))


if __name__ == '__main__':
    # Process the file using procedures defined above.
    stack.append(sys.argv[1])
    read_file()
    filter_characters()
    scan()
    remove_stopwords()
    frequencies()
    sort()
    # ...
    stack.append(0)
    while stack[-1] < 25 and len(stack) > 1:
        heap['i'] = stack.pop()
        (word, frequency) = stack.pop()
        print(word, '-', frequency)
        stack.append(heap['i'])
        stack.append(1)
        stack.append(stack.pop() + stack.pop())

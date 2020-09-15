    Copyright(c) 2020-
    Author: Chaitanya Tejaswi (github.com/CRTejaswi)    License: GPL v3.0+

# Elements of Style
> Constrained Python3 solutions to a problem. <br>
> Based on [Exercises in Programming Style](https://github.com/crista/exercises-in-programming-style) by [Cristina Lopez](http://tagide.com/about.html). <br>

# The Problem

Given a text file, produce a list of words with their frequencies, printing 'N=25' of them out in a decreasing order of frequency. <br>
Make sure to "lowercase" everything, and ignore stopwords (the, for, in, ...). <br>

# The Result

```
PS> py .\test.py .\pride-and-prejudice.txt

mr - 786
elizabeth - 635
very - 488
darcy - 418
such - 395
mrs - 343
much - 329
more - 327
bennet - 323
bingley - 306
jane - 295
miss - 283
one - 275
know - 239
before - 229
herself - 227
though - 226
well - 224
never - 220
sister - 218
soon - 216
think - 211
now - 209
time - 203
good - 201
```

# Index

- [01](#01)
- [02](#02)

## 01

__Constraints__ <br>

- Fixed primary memory-size (eg. 1024 memory-blocks)
- No identifiers - no variables or tagged memory addresses. Memory can be accessed only through each of these numbered locations.
```python
#!/usr/bin/env python3
import os
import sys


def touchopen(f, *args, **kwargs):
    try:
        os.remove(f)
    except OSError:
        pass
    open(f, "a").close()
    return open(f, *args, **kwargs)


def style1():
    '''
    data[0]    = list of stopwords
    data[1]    = single line from input file (~80 characters)
    data[1][0] = data[1] is a list; this is the actual line as a string
    data[2]    = index of startCharacter of word
    data[3]    = index of characters of current word
    data[4]    = flag; indicates if word was found
    data[5]    = current word
    data[6]    = word,frequency from word_frequencies file (secondary memory)
    data[7]    = frequency of occurence of word
    '''
    data = []
    with open('stopwords.txt') as f:
        data = [f.read(1024).split(',')]
    data.append([])
    data.append(None)
    data.append(0)
    data.append(False)
    data.append('')
    data.append('')
    data.append(0)

    '''
    - append '\n' to line if it doesn't exist
    - make data[2] = 0 (start index of current word) if any alphanumeric character is encountered.
    - if the character isn't alphanumeric (=> end of word), process the word.
        - select line from start:stop index. make it lowercase.
        - don't process single-letter words or stopwords.
        - match currentWord with each word from word_frequencies file.
            - start by simply appending the word to file after checking the match flag (data[4]).
            - every consequent match => set the match flag (data[4]) and increment the frequency (data[7]) by 1.
            -
    '''
    word_frequencies = touchopen('word_frequencies', 'rb+')
    with open(sys.argv[1], 'r') as f:
        while True:
            data[1] = [f.readline()]
            if data[1] == ['']:
                break
            if data[1][0][len(data[1][0]) - 1] != '\n':
                data[1][0] += '\n'
            data[2] = None
            data[3] = 0
            for character in data[1][0]:
                if data[2] == None:
                    if character.isalnum():
                        data[2] = data[3]
                else:
                    if not character.isalnum():
                        data[4] = False
                        data[5] = data[1][0][data[2]:data[3]].lower()
                        if len(data[5]) >= 2 and data[5] not in data[0]:
                            while True:
                                data[6] = str(word_frequencies.readline().strip(), 'utf-8')
                                if data[6] == '':
                                    break
                                data[7] = int(data[6].split(',')[1])
                                data[6] = data[6].split(',')[0].strip()
                                if data[5] == data[6]:
                                    data[7] += 1
                                    data[4] = True
                                    break
                            if not data[4]:
                                word_frequencies.seek(0, 1)
                                word_frequencies.write(bytes("%20s,%04d\n" % (data[5], 1), 'utf-8'))
                            else:
                                word_frequencies.seek(-26, 1)
                                word_frequencies.write(bytes("%20s,%04d\n" % (data[5], data[7]), 'utf-8'))
                            word_frequencies.seek(0, 0)
                        data[2] = None
                data[3] += 1
    word_frequencies.flush()

    '''
    data[0-24] = top 25 words from word_frequencies file.
    data[25]   = word,frequency from word_frequencies file.
    data[26]   = frequency of this word.
    '''
    del data[:]
    data += [[]] * (25 - len(data))
    data.append('')
    data.append(0)
    while True:
        data[25] = str(word_frequencies.readline().strip(), 'utf-8')
        if data[25] == '':
            break
        data[26] = int(data[25].split(',')[1])
        data[25] = data[25].split(',')[0].strip()
        for i in range(25):
            if data[i] == [] or data[i][1] < data[26]:
                data.insert(i, [data[25], data[26]])
                del data[26]
                break
    for tf in data[0:25]:
        if len(tf) == 2:
            print(tf[0], '-', tf[1])
    word_frequencies.close()


if __name__ == '__main__':
    style1()
```

## 02

__Constraints__ <br>

- Implement primary/secondary memory operations on a stack/heap respectively.
- Implement all functionality using procedures - names associated with a set of instructions.

```python
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
        (w, f) = stack.pop()
        print(w, '-', f)
        stack.append(heap['i'])
        stack.append(1)
        stack.append(stack.pop() + stack.pop())
```


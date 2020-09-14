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
    print(f'Data:{data}')
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
        - don't process the word if if is 1-2 character long, or a stopword.
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

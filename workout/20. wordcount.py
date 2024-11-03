# The challenge for this exercise is to write a wordcount function that mimics the wc Unix command. The function will take a filename as input and will print four lines of output:
#
# Number of characters (including whitespace)
#
#     Number of words (separated by whitespace)
#
#     Number of lines
#
# Number of unique words (case sensitive, so “NO” is different from “no”)

path = 'C:/Users/user/Downloads/wcfile.txt'

def wordcount(filepath):
    worddic = {'charcount': 0, 'wordcount': 0, 'linecount': 0,  'unique_words' : 0}

    unique_words = set()
    with open(filepath) as f:
        for line in f:
            worddic['linecount'] += 1
            worddic['charcount'] += len(line)
            line = line.strip()
            if line:
                words_in_line = line.split(' ')
                worddic['wordcount'] += len(words_in_line)
                unique_words.update(words_in_line)
    worddic['unique_words'] = len(unique_words)

    for key, value in worddic.items():
        print(f'{key}:{value}')
wordcount(path)


# Ask the user to enter the name of a text file
# and then (on one line, separated by spaces)
# words whose frequencies should be counted in that file.
# Count how many times those words appear in a dict,
# using the user-entered words as the keys and the counts as the values.

def input_wordcount():
    filename = input('enter filename:')
    words = input('enter words (separated by spaces):').rstrip().split(' ')
    worddict = {word:0 for word in words}
    with open(filename) as f:
        for line in f:
            words_in_line = line.strip().split(' ')
            for word in words_in_line:
                if word in worddict.keys():
                    worddict[word] += 1
    for key, value in worddict.items():
        print(f'{key}:{value}')


#input_wordcount()


# Create a dict in which the keys are the names of files on your system
# and the values are the sizes of those files.
# To calculate the size, you can use os.stat (http://mng.bz/dyyo).

# -> only did it for one directory

import os
def filestat():
    dir_path = 'C:/Users/user/Downloads'
    files = os.listdir(dir_path)
    filedict = {file: os.stat(dir_path + '/' + file).st_size for file in files}

    for key, value in filedict.items():
        print(f'{key}:{value}')

# filestat()



# Given a directory, read through each file and count the frequency of each letter.
# (Force letters to be lowercase, and ignore nonletter characters.)
# Use a dict to keep track of the letter frequencies.
# What are the five most common letters across all of these files?

import string
def dirstat(dir_path):
    files = os.listdir(dir_path)
    letterdict = {letter : 0 for letter in string.ascii_lowercase}
    for file in files:
        if file.endswith('txt'):
            with open(dir_path+'/'+file) as f:
                for line in f:
                    line = line.lower()
                    for char in line:
                        if char in letterdict.keys():
                            letterdict[char] += 1
    letterdict = {key:value for key, value in sorted(letterdict.items(), key = lambda item:-item[1])}
    i = 0
    for key, value in letterdict.items():
        if i<5:
            print(f'{key}:{value}')
            i+=1
        else:
            break

dirstat('C:/Users/user/Downloads')



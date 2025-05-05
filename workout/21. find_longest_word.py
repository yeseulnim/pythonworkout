# in this exercise, write two functions
# find_longest_word takes a filename as an argument
# and returns the longest word found in the file.
# the second function, find_all_longest_words,
# takes a directory name and returns a dict in which
# the keys are filenames and the values are the longest words from each file

import os
import re

def find_longest_word(filename):
    max_length = 0
    longest_word = ""
    with open(filename) as f:
        for line in f:
            separators = r"[\—\-/,;!?.\s]+"
            words = re.split(separators, line)
            for word in words:
                if len(word)>max_length:
                    max_length = len(word)
                    longest_word = word
    return longest_word

def find_all_longest_words(dirname):
    files = os.listdir(dirname)
    longest_words = [find_longest_word(dirname + f) for f in files]
    longest_words_dict = dict(zip(files,longest_words))
    return longest_words_dict

dir_path = 'C:/Users/user/Downloads/books/'

print(find_all_longest_words(dir_path))


# Use the hashlib module in the Python standard library, and the md5 function within it,
# to calculate the MD5 hash for the contents of every file in a user specified directory
# Then print all of the filenames and their MD5 hashes

import hashlib

def filename_plus_md5(dirname):
    files = os.listdir(dirname)
    md5s = [hashlib.md5(f.encode('utf-8')).hexdigest() for f in files]
    return dict(zip(files, md5s))

print(filename_plus_md5(dir_path))

# ask the user for a directory name
# show all of the files in the directory,
# as well as how long ago the directory was modified

import arrow

def filename_plus_most_recent_modified():
    dir = input("please input directory name: ")
    # show all of the files in the directory
    files = os.listdir(dir)
    print(files)
    # show how long ago the directory was modified
    modified_ts = os.stat(dir).st_mtime
    modified = arrow.get(modified_ts)
    print(modified.humanize())

#filename_plus_most_recent_modified()


# Open an HTTP server's log file.
# Summarize how many requests resulted in numeric response codes

filepath = 'C:/Users/user/Downloads/mini-access-log/mini-access-log.txt'

def summarize_numeric_response_codes(filename):
    response_codes = dict()
    with open(filename) as f:
        for line in f:
            words = line.split("\"")
            response = words[2].split(" ")[1]
            if response in response_codes.keys():
                response_codes[response] += 1
            else:
                response_codes[response] = 1
    return response_codes

print(summarize_numeric_response_codes(filepath))













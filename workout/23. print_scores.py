# there's a scores directory on the filesystem containing a number of files in JSON format.
# Each file represents the score for one class.
# write a function, print_scores, that takes a directory name as an argument
# and prints a summary of the student scores it finds

import json
import os

path = "C:/Users/user/Downloads/scores"

def print_scores(dir):
    scores = {}
    files = os.listdir(dir)
    for file in files:
        scores[file] = {}
        filepath = os.path.join(dir,file)
        with open(filepath, 'r') as f:
            data = json.load(f)
            for subject, metrics in data.items():
                scores[file].setdefault(subject, [])
                metrics_values = metrics.values()
                for value in metrics_values:
                    scores[file][subject].append(value)
    for one_class in scores:
        print(one_class)
        for subject, subject_scores in scores[one_class].items():
            min_score = min(subject_scores)
            max_score = max(subject_scores)
            avg_score = (sum(subject_scores)/len(subject_scores))

            print(subject)
            print(f'\tmin {min_score}')
            print(f'\tmax {max_score}')
            print(f'\tavg {avg_score}')

#print_scores(path)


# convert /etc/passwd from a csv-style file into a json-formatted file.
# the json file will contain the equivalent of a list of python tuples,
# with each tuple representing one line from the file.

import csv
def csv_to_json(path):
    data = []
    with open(path,'r') as f:
        for line in f:
            items = tuple([item.strip() for item in line.split(',')])
            data.append(items)
    with open("23_json.json", 'w') as f:
        json.dump(data, f)

csv_to_json("22_dict.csv")


# for a slightly different challenge, turn each line in the file into a python dict.
# this will require identifying each field with a unique column or key name

def csv_to_json_dict(path):
    data = []
    with open(path,'r') as f:
        for line in f:
            items = tuple([item.strip() for item in line.split(',')])
            items_dict = {items[0]:items[1:]}
            data.append(items_dict)
    with open("23_json_dict.json", 'w') as f:
        json.dump(data, f)

csv_to_json_dict("22_dict.csv")


# ask the user for the name of a directory. iterate through each file in that directory
# (ignoring subdirectories), getting (via os.stat) the size of the file and when it was
# last modified. Create a JSON-formatted file on disk listing each filename, size,
# and modification timestamp. Then read the file back in, and identify which files were
# modified most and least recently, and which files are largest and smallest, in that directory.

import arrow

def summarize_directory():
    dirname = input("input directory name:")
    file_dict = {}
    files = os.listdir(dirname)
    for file in files:
        file_path = os.path.join(dirname, file)
        file_info = os.stat(file_path)

        file_size = file_info.st_size
        file_mod_ts = file_info.st_mtime

        file_dict[file] = [file_size, file_mod_ts]
    with open("23_json_summ.json", 'w') as f:
        json.dump(file_dict, f)


#summarize_directory()


def read_summary(filepath):


    with open(filepath,'r') as f:
        data = json.load(f)

        largest_file = ""
        smallest_file = ""
        max_size = 0
        min_size = float('inf')

        most_recent_file = ""
        least_recent_file = ""
        max_date = 0
        min_date = float('inf')

        for filename, info in data.items():
            file_size = info[0]
            ts = info[1]

            if file_size>max_size:
                max_size = file_size
                largest_file = filename
            if file_size<min_size:
                min_size = file_size
                smallest_file = filename

            if ts>max_date:
                max_date = ts
                most_recent_file = filename
            if ts<min_date:
                min_date = ts
                least_recent_file = filename

    print(f"largest file : {largest_file}")
    print(f"smallest file : {smallest_file}")
    print(f"most recently modified file: {most_recent_file}")
    print(f"least recentlymodified file: {least_recent_file}")

read_summary('23_json_summ.json')









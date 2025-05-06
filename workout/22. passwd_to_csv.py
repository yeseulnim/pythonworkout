# create a function, passwd_to_csv,
# that takes two filenames as arguments:
# the first is a passwd-style file to read from,
# and the second is the name of a file in which to write the output

import csv
def passwd_to_csv(infile, outfile):
    outfile_list = []
    with open(infile) as f:
        for line in f:
            words = line.split(':')
            if len(words)>2:
                outfile_list.append([words[0], words[2]])

    with open(outfile,'w', newline = '') as f:
        o = csv.writer(f, delimiter='\t')
        for row in outfile_list:
            o.writerow(row)

passwd_to_csv("22_text.txt","22_csv.csv")


# ask the user to enter a space-separated list of integers
# indicating which fields should be written to the output csv file
# also ask the user which caracter should be used as a delimiter in the output file
# then read from /etc/passwd, writing the user's chosen fields,
# separated by the user's chosen delimiter

def passwd_to_csv_2(infile, outfile):
    field1 = int(input("which field should come first?:"))
    field2 = int(input("which field should come second?:"))
    delim = input("input delimiter: ")
    outfile_list = []
    with open(infile) as f:
        for line in f:
            words = line.split(':')
            if len(words) > 2:
                outfile_list.append([words[field1], words[field2]])

    with open(outfile, 'w', newline='') as f:
        o = csv.writer(f, delimiter = delim )
        for row in outfile_list:
            o.writerow(row)


#passwd_to_csv_2("22_text.txt", "22_csv_2.csv")



# write a function that writes a dict to a csv file
# each line in the csv file should contain three fields :
# (1) the key, which we'll assume to be a string,
# (2) the value,
# and (3) the type of the value (e.g., str or int)

sample_dict = {"kse": 1, "bsh" : 2, "gye": "unknown"}

def dict_to_csv(dic):
    with open("22_dict.csv", 'w', newline = '') as f:
        o = csv.writer(f)
        for (key, value) in sample_dict.items():
            o.writerow([key, value, type(value)])

dict_to_csv(sample_dict)


# create a csv file, in which each line contains 10 random integers
# between 10 and 100.
# now read the file back, and print the sum and mean of the numbers on each line

from random import randint
def lines_to_csv():
    num_of_lines = int(input("input number of lines:"))
    with open("22_csv_3.csv",'w', newline = '') as f:
        o = csv.writer(f)
        for i in range(num_of_lines):
            line = [randint(10, 100) for i in range(10)]
            o.writerow(line)

def csv_to_calc(filename):
    with open(filename,'r') as f:
        for line in f:
            ints = map(int,line.split(","))
            sum_of_ints = sum(ints)
            print(sum_of_ints, sum_of_ints/10)

lines_to_csv()
csv_to_calc("22_csv_3.csv")

















# write a function (get_final_line) that takes a filename as an argument
# the function should return that file's final line on the screen

def get_final_line(filepath):
    lastline = ""
    for line in open(filepath):
        lastline = line
    return lastline

filepath = "C:/Users/user/Downloads/Noto_Serif_KR/OFL.txt"

print(get_final_line(filepath))

# Iterate over the lines of a text file
# Find all of the words that contain only integers, and sum them
def get_integer_sum(filepath):
    integer_sum = 0
    for line in open(filepath):
        words = line.split(' ')
        for word in words:
            try:
                integer_sum += int(word)
            except:
                pass
    return integer_sum

print(get_integer_sum(filepath))

# create a text file containing two tab-separated columns
# with each column containing a number
# then use python to read through the file you've created
# for each line, multiply each first number by the second
# then sum the results from all the lines
# ignore any line that doesn't contain two numeric columns

f = open('18_text.txt','w')
text = '''1\t3
2\t4
3\t5
a\tb
100\t50\t99'''
f.write(text)
f.close()

def get_multiple_sum(filepath):
    multiple_sum = 0
    with open(filepath) as f:
        for line in f:
            line = line.rstrip()
            words = line.split('\t')
            if len(words) == 2:
                try:
                    multiple_sum += (int(words[0]) * int(words[1]))
                except:
                    pass
    f.close()
    return multiple_sum

print(get_multiple_sum('18_text.txt'))

# read through a text file, line by line
# use a dict to keep track of how many times each vowel appears in the file
# print the resulting tabulation

def vowels_used(filepath):
    vowel_dict = {key:0 for key in ['a','e','i','o','u']}
    with open(filepath) as f:
        for line in f:
            for char in line:
                if char in 'aeiou':
                    vowel_dict[char] += 1
    return vowel_dict

print(vowels_used(filepath))




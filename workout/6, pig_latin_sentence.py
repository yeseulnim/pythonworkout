# write a function called pl_sentence that takes a string
# containing several words, separated by spaces.
# (to make things easier, there will be no capital letters or punctuations.)
# print the output on a single line.

def pl_sentences(sentence:str):
    word_list = sentence.split()
    for ind, word in enumerate(word_list):
        if word[0] in "aeiou":
            word_list[ind] = word + "way"
        else:
            word_list[ind] = word[1:] + "ay"
    return " ".join(word_list)

print(pl_sentences("i eat chicken for dinner"))


# take a text file, creating and printing a nonsensical sentence
# from the nth word on each of the first 10 lines
# where n is the line number

def read_nth_word(filepath:str):
    f = open(filepath, 'r')
    nth_words = []
    for n in range(10):
        line = f.readline()
        word_list = line.split()
        try:
            nth_words.append(word_list[n])
        except:
            pass
    f.close()

    return " ".join(nth_words)

filepath = "C:/Users/user/Downloads/Noto_Serif_KR/OFL.txt"
print(read_nth_word(filepath))

# Write a function that transposes a list of strings
# in which each string contains multiple words separated by whitespace.
# Specifically, it should perform in such a way that if you were to pass
# the list ['abc def ghi' 'jkl mno pqr' 'stu vwx yz'] to the function,
# it would return ['abc jkl stu' 'def mno vwx' 'ghi pqr yz']

def transpose(word_list:list):
    nested_list = [row.split() for row in word_list]

    row_len = len(nested_list[0])
    col_len = len(nested_list)
    final_row_len, final_col_len = col_len, row_len
    result = []
    for row_num in range(final_row_len):
        row = [row[row_num] for row in nested_list]
        result.append(row)
    # using map and zip + * can result in a simpler solution
    # result = list(map(list,zip(*nested_list)))
    return result

print(transpose(['abc def ghi','jkl mno pqr','stu vwx yz']))


# read through an apache logfile.
# if there's a 404 error - you can just search for 404 if you want -
# display the ip address, which should be the first element.


filepath = "C:/Users/user/Documents/sample_log.log"
def apache_log_404_ip(filepath:str):
    f = open(filepath, 'r')
    while True:
        line = f.readline()
        if not line: break
        line_list = line.split()
        if line_list[-2] == "404":
            return line_list[0]
    return None

print(apache_log_404_ip(filepath))



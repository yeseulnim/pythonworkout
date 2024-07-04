# write a function, strsort, that takes a single string as its input
# and returns a string.
# the returned string should contain the same characters as the input,
# except that its characters should be sorted in order
# from the lowest unicode value to the highest unicode value.

def strsort(sentence:str):
    output = sorted(sentence)
    return "".join(output)

print(strsort("cba"))
print(strsort("c b a'"))


# given the string "tom dick harry" break into individual words
# and then sort those words alphabetically
# once they are sorted, print them with commas between the names

def namesort(sentence:str):
    output = sorted(sentence.split())
    return ", ".join(output)
print(namesort("Tom Dick Harry"))


# which is the last word, alphabetically, in a text file?
def last_word(filepath:str):
    f = open(filepath, 'r')
    output = sorted(f.read().split())[-1]
    f.close()
    return output
print(last_word("C:/Users/user/Downloads/Noto_Serif_KR/OFL.txt"))


# which is the longest word in a text file?
def longest_word(filepath:str):
    f = open(filepath, 'r')
    output = sorted(f.read().split(), key=len)[-1]
    f.close()
    return output
print(longest_word("C:/Users/user/Downloads/Noto_Serif_KR/OFL.txt"))

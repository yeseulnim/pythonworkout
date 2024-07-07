# write a function, alphabetize_names, that assumes the existence
# of a people constant defined as shown in the code.
# the function should return the list of dicts,
# but sorted by last name and then by first name.

PEOPLE = [{'first':'Joe','last':'Biden','email':'president@whitehouse.gov'},
          {'first':'Vlad','last':'Putin','email':'president@kremvax.ru'},
          {'first':'Reuven','last':'Lerner','email':'reuven@lerner.co.il'}]

def alphabetize_names(names):
    names.sort(key = lambda x : (x['last'], x['first']))
    return names
print(alphabetize_names(PEOPLE))

# another solution
import operator
def alphabetize_names2(names):
    names = sorted(names, key = operator.itemgetter('last','first'))
    return names
print(alphabetize_names2(PEOPLE))


# given a sequence of positive and negative numbers,
# sort them by absolute value
def sort_abs(val_seq):
    val_seq = list(val_seq)
    val_seq.sort(key = lambda x:abs(x))
    return val_seq
print(sort_abs([1,2,3,4,-5,-6]))
print(sort_abs((1,2,3,4,-5,-6)))

# given a list of strings, sort them according to how many vowels they contain
def sort_vowel_count(str_seq):
    return sorted(str_seq, key = lambda x: sum(x.count(vowel) for vowel in "aeiou"))
print(sort_vowel_count(["ahaha","abbb","ggggaa"]))

# given a list of lists, with each list containing zero or more numbers,
# sort by the sum of each inner list's numbers
def sort_sum(num_seq):
    return sorted(num_seq, key = lambda x: sum(int(i) for i in x if i.isdigit()))
print(sort_sum(["456","1a2b3c"]))

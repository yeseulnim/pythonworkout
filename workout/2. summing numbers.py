# build a function 'mysum' that does the same thing as sum
# however, instead of taking a single sequence as a parameter,
# it should take a variable number of arguments

def mysum(*args):
    sum_num = 0
    for val in args:
        sum_num += val
    return sum_num

# print(mysum(1,2,3))

# The build-in sum takes an optional second argument, which is used as the starting point for summing
# that's why it takes a list of numbers as its first argument ex. sum([1.2.3].4)
# reimplement mysum such that it works this way
# if a second argument is not provided, it should default to 0
# just take two arguments a list an and optional starting point

def mysum2(nums, starting_point = 0):
    sum_num = starting_point
    for val in nums:
        sum_num += val
    return sum_num

#print(mysum2([1,2,3],4))


# write a functino that takes a list of numbers and returns the average of these numbers
def mymean(nums):
    sum_num = 0
    for val in nums:
        sum_num += val
    mean = sum_num/len(nums)
    return mean

#print(mymean([1,2,3]))



# write a function that takes a string and returns a tuple consisting of three integers
# representing the length of the shortest word, the longest word, and the average word length

def mywords(sentence):
    sentence = sentence.split()
    shortest = len(sentence[0])
    longest = len(sentence[0])
    len_sum = 0
    word_count = 0

    for word in sentence:
        word_len = len(word)
        if word_len < shortest:
            shortest = word_len
        if word_len > longest:
            longest = word_len
        len_sum +=  word_len
        word_count += 1

    return (shortest, longest, len_sum/word_count)

#print(mywords("a short cat jumped over the moon"))




# write a function that takes a list of python objects.
# sum the objects that are integers or can be turned into integers
# ignore others

def myobjectsum(objects):
    sum_num = 0
    for val in objects:
        try:
            sum_num += int(val)
        except:
            pass
    return sum_num


#print(myobjectsum(["a", 1, 2.0]))





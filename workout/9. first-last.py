# write a function, firstlast, that takes a sequence (string,list,or tuple)
# and returns the first and last elements of that sequence,
# in a two-element sequence of the same type.

def firstlast(sequence):
    return sequence[:1] + sequence[-1:]

print(firstlast([1,2,3,4,5]))
print(firstlast((1,2,3,4,5)))
print(firstlast("1,2,3,4,5"))

# don't write one function that squares integers,
# and another that squares floats.
# write one function that handles all numbers

def square(num):
    return num**2

print(square(3))
print(square(3.0))

# don't write one function that finds the largest element of a string,
# another that does the same for a list, and a third that does the same for a tuple.
# write just one function that works on all of them

def largest(sequence):
    return max(sequence)

print(largest([1,2,3,4,5]))
print(largest((1,2,3,4,5)))
print(largest("1,2,3,4,5"))

# don't write one function to find the largest word in a file that works on files
# and another that works on the io.StringIO file simulator used in testing.
# write one function that works on both.

import io
output = io.StringIO('first line \n second line')

filepath = "C:/Users/user/Downloads/Noto_Serif_KR/OFL.txt"
f = open(filepath, 'r')

def largestword(file):
    content = file.read().split()
    file.close()
    return max(content)

print(largestword(output))
print(largestword(f))

# write a function that takes a list or tuple of numbers
# return a two-element list, containing(respectively)
# the sum of the even-indexed numbers
# and the sum of the odd_indexed numbers
def even_odd_sums(sequence):
    output = [0,0]
    for idx, num in enumerate(sequence):
        if idx%2==0:
            output[0] += num
        else:
            output[1] += num
    return output

print(even_odd_sums([10,20,30,40,50,60]))
print(even_odd_sums((10,20,30,40,50,60)))


# write a function that takes a list or tuple of numbers.
# return the result of alternatively adding and subtracting the numbers from each other.

def plus_minus(sequence):
    output = sequence[0]
    for idx,num in enumerate(sequence[1:]):
        if idx%2==0:
            output+=num
        else:
            output-=num
    return output
print(plus_minus([10,20,30,40,50,60]))

# write a function that partly emulates the built-in zip function
# taking any number of iterables and returning a set of tuples
# each tuple will contain one element from each of the iterables passed to the function
# you can return a list and can assume that all of the iterables are of the same length

def myzip(sequence1, sequence2):
    output = []
    for idx, num in enumerate(sequence1):
        output.append(tuple((num, sequence2[idx])))
    return output
print(myzip([10,20,30],'abc'))





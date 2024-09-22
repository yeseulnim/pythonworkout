# write a function, dictdiff, that takes two dicts s arguments
# the function returns a new dict that expresses the difference between the two dicts
# if there are no differences between the dicts, dictdiff returns an empty dict
# for each key-value that differs, the return value of dictdif will have a key-value pair
# in which the value is a list containing the values from the two different dicts
# if one of the dicts doesn't contain that key, it should contain None

d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}
d3 = {'a':1, 'b':2, 'd':3}
d4 = {'a':1, 'b':2, 'd':4}

def dictdiff(dict1, dict2):
    output = {}
    all_keys = dict1.keys() | dict2.keys() # Union : |
    for key in all_keys:
        value1 = dict1.get(key, None)
        value2 = dict2.get(key, None)
        if value1 != value2:
            output[key] = [value1, value2]
    return output

print(dictdiff(d1,d1))
print(dictdiff(d1,d2))
print(dictdiff(d3,d2))
print(dictdiff(d1,d4))


# the dict.update method merges two dicts.
# write a function that takes any number of dicts and returns a dict
# that reflects the combination of all of them
# if the same key appears in more than one dict
# then the most recently merged dict's value should appear in the output

d5 = {'a':10, 'e':30}
def dict_update(dict1, *dicts):
    for dict in dicts:
        dict1.update(dict)
    return dict1

print(dict_update(d1,d3, d5))


# write a function that takes any even number of arguments
# and returns a dict based on them
# the even-indexed arguments become the dict keys
# while the odd-numbered arguments become the dict values

def dict_create(*items):
    output = {}
    for i in range(int(len(items)/2)):
        output[items[i*2]] = items[i*2+1]
    return output

print(dict_create('a',1,'b',2))


# write a function, dict_partition, that takes one dict(d) and a function(f) as arguments
# dict_partition will return two dicts, each containing key-value pairs from d
# the decision regarding where to put each of the key-value pairs will be made
# according to the output from f
# which will be run on each key-value pair on d
# if f returns true, then the key-value pair will be put in the first output dict
# if f returns false, then the key-value pair will be put in the second output dict

d = {'david' : 5, 'elizabeth': 8, 'daniels' : 6}
def f(key, value):
    if len(key) == value:
        return True
    return False

def dict_partition(d, f):
    d1 = {}
    d2 = {}
    for key,value in d.items():
        if f(key,value):
            d1[key] = value
        else:
            d2[key] = value
    return d1, d2

print(dict_partition(d,f))


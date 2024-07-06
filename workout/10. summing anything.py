# redefine the mysum function we defined earlier
# such that it can take any number of arguments
# the arguments must be all of the same type
# and know how to respond to the + operator.
# thus, the function should work with numbers, strings, lists, and tuples
# but not with sets and dicts.
def mysum(*items):
    if not items:
        return items
    output = items[0]
    for item in items[1:]:
        output += item
    return output

print(mysum("abc","def"))
print(mysum(1,2,3))
print(mysum([1,2,3],[4,5,6]))


# write a function mysum_bigger_than that works the same as mysum
# except that it takes a first argument that precedes *args.
# that argument indicates the threshold for including an argument in the sum.
# thus, calling mysum_bigger_than(10,5,20,30,6) would return 50 -
# because 5 and 6 aren't greater than 10.

def mysum_bigger_than(limit, *items):
    items = [item for item in items if item>limit]
    output = items[0]
    for item in items[1:]:
        output += item
    return output

print(mysum_bigger_than(10,5,20,30,6))
print(mysum_bigger_than("bbb","abc","def","xyz"))


# write a function sum_numeric that takes any numbber of arguments.
# if the argument is or can be turned into an integer,
# then it sould be added to the total.

def sum_numeric(*items):
    output = 0
    for item in items:
        try:
            output += int(item)
        except:
            pass
    return output

print(sum_numeric(10,20,"a","30"))


# write a function that takes a list of dicts
# and returns a single dict that combines all of the keys and values
# if a key appears in more than one argument,
# the value should be a list containing all of the values from the argument.

def combine_dict(dics):
    output_dic = dics[0]

    for dic in dics[1:]:
        for key, value in dic.items():
            if (key in output_dic) and (value not in output_dic[key]):
                try:
                    output_dic[key] += [value]
                except:
                    output_dic[key] = list((output_dic[key],value))
            else:
                output_dic[key] = value
    return output_dic

dict_a = {'France':'Paris','USA':'Orlando','Japan':'Tokyo'}
dict_b = {'USA':'Orlando', 'Japan':'Kyoto'}
print(combine_dict([dict_a,dict_b]))

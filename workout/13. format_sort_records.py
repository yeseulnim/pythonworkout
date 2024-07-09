# write a python function, format_sort_records, that takes the PEOPLE list
# and returns a formatted string that looks like the following:
# (excerpt in book)
# each name should be printed in a 10-character field
# time should be printed in a 5-character field
# with one space of padding between each of the columns
# time should only display 2 digits after the decimal point

PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]

def format_sort_records(seq_list):
    formatted_strings = []
    for seq in seq_list:
        one_formatted_string = f"{seq[1]:10} {seq[0]:10} {seq[2]:5.2f}"
        formatted_strings.append(one_formatted_string)
    return "\n".join(formatted_strings)

print(format_sort_records(PEOPLE))

# reimplement this exercise using namedtuple objects defined in the collection module
from collections import namedtuple
def format_sort_records_2(seq_list):
    formatted_strings = []
    for seq in seq_list:
        leaders = namedtuple('Leaders', ['first_name', 'last_name', 'travel_time'])
        seq = leaders(seq[0], seq[1], seq[2])
        one_formatted_string = f"{seq.last_name:10} {seq.first_name:10} {seq.travel_time:5.2f}"
        formatted_strings.append(one_formatted_string)
    return "\n".join(formatted_strings)

print(format_sort_records_2(PEOPLE))

# Define a list of tuples, in which each tuple contains the name, length(in mins), and director
# of the movies nominated for best feature Oscar awards last year.
# Ask the user whether they want ot sort the list by title, length, or director's name
# then present the list sorted by the user's choice of axis

FILMS = [('Oppenheimer', 180, 'Nolan'),
         ('Barbie', 113, 'Gerwig'),
         ('The Zone of Interest', 105, 'Glazer'),
         ('Maestro', 129, 'Cooper'),
         ('Anatomy of a Fall', 152, 'Triet')]
def sort_films(seq_list):
    axis = int(input("In which order do you want to sort the nominees?\n"
                 "Press 1 for 'Title'\n"
                 "Press 2 for 'Runtime'\n"
                 "Press 3 for 'Director'"))
    axis -= 1
    print(sorted(seq_list, key = lambda x: x[axis]))

#sort_films(FILMS)

# extend this exercise by allowing the user to sort by two or three of these fields
# the user can specify the fields by entering them separated by commas
# you can use str.split to turn them into a list

def sort_films_2(seq_list):
    axises = input("In which orders do you want to sort the nominees?\n"
                     "Choose 1 for 'Title'\n"
                     "Choose 2 for 'Runtime'\n"
                     "Choose 3 for 'Director'\n"
                     "Type your answer like this: 1, 2 \n"
                     "Type your answer then press enter: ")
    axis_1, axis_2 = axises.split(",")
    axis_1 = int(axis_1) -1
    axis_2 = int(axis_2) -1
    print(sorted(seq_list, key = lambda x: (x[axis_1], x[axis_2])))

sort_films_2(FILMS)
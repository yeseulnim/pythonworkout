
path = "C:/Users/user/Downloads/passwd.txt"

def passwd_to_dict(path):
    d = {}
    with open(path) as f:
        for line in f:
            if not line.startswith(("#",'\n')):
                line = line.split(":")
                d[line[0]] = int(line[2])
    return d

print(passwd_to_dict(path))

# Read through /etc/passwd, creating a dict in which
# user login shells (the final field on each line) are the keys.
# Each value will be a list of the users for whom
# that shell is defined as their login shell.

def shell_to_dict(path):
    d = {}
    with open(path) as f:
        for line in f:
            if not line.startswith(("#",'\n')):
                line = line.split(":")
                d[line[-1]] = d.get(line[-1],[]) + [line[0]]
    return d

print(shell_to_dict(path))

# Ask the user to enter integers, separated by spaces.
# From this input, create a dict whose keys are the factors for each number,
# and the values are lists containing those of the users’ integers
# that are multiples of those factors.

def integer_to_dict():
    d = {}
    while num := input("Enter integer:"):
        num = int(num)
        for i in range(2, int((num**0.5)//1)+1):
            if num%i==0:
                d[i] = d.get(i, []) + [num]
                d[int(num/i)] = d.get(int(num/i), []) + [num]

    print(d)

# integer_to_dict()


# From /etc/passwd, create a dict in which the keys are the usernames (as in the main exercise)
# and the values are themselves dicts with keys (and appropriate values)
# for user ID, home directory, and shell.


def dict_to_dict(path):
    d = {}
    with open(path) as f:
        for line in f:
            if not line.startswith(("#",'\n')):
                line = line.split(":")
                dd = {"User ID" : line[-3], "Home Directory" : line[-2], "Shell" : line[-1]}
                d[line[0]] = dd
    return d
print(dict_to_dict(path))

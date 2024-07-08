# write a function, most_repeating_word,
# that takes a sequence of strings as input.
# the function should return the string that contains the
# greatest number of repeated letters.
# in other words:
# for each word, find the letter that appears the most times.
# find the word whose most-repeated letter appears more than others.

# * used two functions per the book's suggestion

from collections import Counter
def most_repeating_letter_count(word):
    return Counter(word).most_common(1)[0][1]
def most_repeating_word(seq):
    return max(seq, key = most_repeating_letter_count)

print(most_repeating_word(["abc","edf","elementary","gagagugu"]))

# find the word with the greatest number of repeated vowels
def most_repeating_vowel_count(word):
    vowels = [i for i in word if i in "aeiou"]
    return Counter(vowels).most_common(1)[0][1]
def most_repeating_vowel(seq):
    return max(seq, key = most_repeating_vowel_count)
print(most_repeating_vowel(["abc","edf","elementary","gagagugu"]))


# write a program to read /etc/passwd on a unix computer.
# the first field contains the username,
# and the final field contains the user's shell, the command interpreter.
# display the shells in decreasing order of popularity,
# such that the most popular shell is shown first.

sample_passwd = '''root:x:0:0:root:/root:/bin/ash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/mail:/sbin/nologin
news:x:9:13:news:/usr/lib/news:/sbin/nologin
uucp:x:10:14:uucp:/var/spool/uucppublic:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
man:x:13:15:man:/usr/man:/sbin/nologin
postmaster:x:14:12:postmaster:/var/mail:/sbin/nologin
cron:x:16:16:cron:/var/spool/cron:/sbin/nologin
ftp:x:21:21::/var/lib/ftp:/sbin/nologin
sshd:x:22:22:sshd:/dev/null:/sbin/nologin
at:x:25:25:at:/var/spool/cron/atjobs:/sbin/nologin
squid:x:31:31:Squid:/var/cache/squid:/sbin/nologin
xfs:x:33:33:X Font Server:/etc/X11/fs:/sbin/nologin
games:x:35:35:games:/usr/games:/sbin/nologin
cyrus:x:85:12::/usr/cyrus:/sbin/nologin
vpopmail:x:89:89::/var/vpopmail:/sbin/nologin
ntp:x:123:123:NTP:/var/empty:/sbin/nologin
smmsp:x:209:209:smmsp:/var/spool/mqueue:/sbin/nologin
guest:x:405:100:guest:/dev/null:/sbin/nologin
nobody:x:65534:65534:nobody:/:/sbin/nologin'''

def get_shell(line):
    username, *discard, shell = line.split(":")
    return shell
def sort_shells(seq):
    shells = [get_shell(line) for line in seq.split("\n")]
    count = sorted(Counter(shells).items(), key = lambda item: -item[1])
    return [i[0] for i in count]

print(sort_shells(sample_passwd))


# for an added challenge, after displaying each shell,
# also show the usernames (sorted alphabetically who use each of those shells

from collections import defaultdict

def get_shell_and_username(line):
    username, *discard, shell = line.split(":")
    return username, shell
def get_usernames_for_shell(seq):
    # list of tuples such as [(username 1, shell 1), (username 2, shell 2)]
    shell_dict = defaultdict(list)
    for username, shell in seq:
        shell_dict[shell].append(username)
    return {shell: sorted(set(users)) for shell, users in shell_dict.items()}
def sort_shells_2(seq):
    shells = [get_shell_and_username(line) for line in seq.splitlines()]
    usernames_per_shell = get_usernames_for_shell(shells)
    return sorted(Counter(usernames_per_shell).items(), key = lambda item: -len(item[1]))
print(sort_shells_2(sample_passwd))





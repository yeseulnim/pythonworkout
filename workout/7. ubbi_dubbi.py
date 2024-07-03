# in ubbi dubbi, every vowel is prefaced with ub
# write a function called 'ubbi_dubbi' that takes a single word as an argument
# it should return a string, the word's translation into ubbi dubbi

def ubbi_dubbi(word:str):
    output = []
    for letter in word:
        if letter in "aeiou":
            output.append("ub"+letter)
        else:
            output.append(letter)
    return "".join(output)

print(ubbi_dubbi("octopus"))


# handle capitalized words
# if a word is capitalized (i.e. the first letter is capitalized, but the rest of the word isn't)
# then the ubbi dubbi translation should be similarly capitalized

def ubbi_dubbi_cap(word:str):
    output = []
    for letter in word.lower():
        if letter in "aeiou":
            output.append("ub"+letter)
        else:
            output.append(letter)
    output = "".join(output)
    return output.title() if word.istitle() else output

print(ubbi_dubbi_cap("Octopus"))


# remove author names
# in academia it is common to remove the author's names from a paper submitted for peer review.
# given a string containing an article and a separate list of strings containing author's names,
# replace all names in the article with __ characters.

def replace_author(article:str, author:str):
    article_words = list(article.split())
    author = list(author.split())
    author_len = len(author)
    for idx in range(len(article_words)-author_len+1):
        if article_words[idx:idx+author_len] == author:
            article_words[idx:idx+author_len] = "__"

    return " ".join(article_words)

sample_article = '''The All-Important Article 
By Author Name
First Paragraph
Second Paragraph'''
sample_author = "Author Name"

print(replace_author(sample_article, sample_author))


# url-encode characters
# in URLs, whe often replace special and nonprintable characters with a %
# followed by the character's ASCII value in hexadecimal
# for example,if a url includes a space character(ascii 32, aka 0x20),
# we replace it with %20
# given a string, url-encode any character that isn't a letter or a number

from string import ascii_letters
def url_encode(url:str):
    url_list = [letter for letter in url]
    for idx, letter in enumerate(url_list):
        if letter not in (ascii_letters) and letter not in ".:/":
           hex_val = hex(ord(letter))[2:]
           url_list[idx] = (f"%{hex_val.upper():>02}")
    return "".join(url_list)

print(url_encode("https://www.sample website.com"))
print(url_encode("www.sa_am_ple.com"))

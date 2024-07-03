# for this exercise, write a python function (pig_latin)
# that takes a string as input,
# assumed to be an English word.
# The function should return the translation of this word into pig latin.
# You may assume that the word contains no capital letters or punctuations.

def pig_latin(sentence:str):
    if sentence[0] in "aeiou":
        return sentence+"way"
    return sentence[1:]+sentence[0]+"ay"

print(pig_latin("eat"))
print(pig_latin("python"))

# handle capitalized words
# if a word is capitalized
# (i.e. the first letter is capitalized, but the rest isn't)
# then the pig latin should be similarly capitalized

def pig_latin_cap(sentence:str):
    is_title = sentence.istitle()
    if sentence[0].lower() in "aeiou":
        result = sentence+"way"
    else:
        result = sentence[1:]+sentence[0]+"ay"
    return result.title() if is_title else result

print(pig_latin_cap("Sentence"))

# Handle punctuation
# if a word ends with punctuation,
# then the punctuation should be shifted to the end of the translated word

def pig_latin_punc(sentence:str):
    is_title = sentence.istitle()
    punc = ""
    if sentence[-1] in ".,!?":
        punc = sentence[-1]
        sentence = sentence[:-1]
    if sentence[0].lower() in "aeiou":
        result = sentence + "way" + punc
    else:
        result = sentence[1:] + sentence[0] + "ay" + punc
    return result.title() if is_title else result

print(pig_latin_punc("sample."))
print(pig_latin_punc("Wahaha!"))

# Consider an alternative version of pig latin
# we don't check to see if the first word is a vowel
# but rather check to see if the word contains two different vowels
# if it does, we don't move the first letter to the end
# because the word "wine" contains two different vowels
# we add "way" to the end of it
# by contrast, the word "wind" contains only one vowel
# so we move "w" to the end and add "ay".


def pig_latin_vowel_num(sentence:str):
    is_title = sentence.istitle()
    punc = sentence[-1] if sentence[-1] in ".,!?" else ""
    sentence = sentence[:-1] if punc else sentence

    vowels = set(char for char in sentence.lower() if char in "aeiou")

    if len(vowels)>1:
        result = sentence + "way" + punc
    else:
        result = sentence[1:] + sentence[0] + "ay" + punc

    return result.title() if is_title else result

print(pig_latin_vowel_num("Wind."))
print(pig_latin_vowel_num("Wine!"))
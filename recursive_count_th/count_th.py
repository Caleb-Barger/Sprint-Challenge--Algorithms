'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, i=0):
    # given a word check how many times the sequence th occurs
    # base case?
    # if i + 1 is greator than the length of
    # the word - 1 than return 0
    if i + 1 > len(word) - 1:
        return 0
    # recursive case?
    # increment i
    # return a call to self where we are returning 1 +
    # whatever the last return value was if we reach
    # a sequence of th
    if word[i] + word[i + 1] == "th":
        i += 1
        return 1 + count_th(word, i)
    # otherwise call self incrementing i
    else:
        i += 1
        return count_th(word, i)
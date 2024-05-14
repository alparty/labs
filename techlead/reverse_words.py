""" Given a list of words in a string, reverse the words in-place (ie don't create a new string and reverse the words). Since python strings are not mutable, you can assume the input will be a mutable sequence (like list). """


def rev(list, s, e):
    while s < e:
        tmp = list[s]
        list[s] = list[e]
        list[e] = tmp
        s += 1
        e -= 1


def reverse_words(words):
    rev(words, 0, len(words) - 1)
    s = 0
    e = 0
    for i in range(s, len(words)):
        if words[i] == " " or i == len(words) - 1:
            e = i - 1 if i < len(words) - 1 else i
            rev(words, s, e)
            s = i + 1
            e = s
            i += 1


s = list("can you read this")
reverse_words(s)
print("".join(s))
# this read you can

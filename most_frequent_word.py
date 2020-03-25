'''
    Most frequent word count program.
    This program assumes all string to be lower-case.

    Runtime: O(m) * O(1) => O(m)
    m = length of string tokenized
'''

def most_freq_word(string) -> dict:
    hashmap = dict()

    for word in string.split(None):
        if word.lower() in hashmap:
            hashmap[word] += 1
        else:
            hashmap.setdefault(word.lower(), 1)
    if len(hashmap) > 0:
        return max(hashmap.items(), key=lambda x: x[1])
    return dict()

if __name__ == '__main__':
    word = 'This is the most frequently used this word in this bloody universe'
    print(most_freq_word(word))

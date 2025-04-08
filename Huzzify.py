vowels = ['a', 'e', 'i', 'o', 'u']

def huzzify(word):
    if no_vowels(word):
        return word + "uzz"
    for i in range(len(word)):
        if word[len(word) - i - 1] in vowels:
            return word[:len(word) - i - 1] + "uzz"
    return word

def huzzify_sentence(sentence):
    sentence_list = sentence.split()
    res = ""
    for i in range(len(sentence_list)):
        sentence_list[i] = huzzify(sentence_list[i])
        res += sentence_list[i] + " "
    return res

def no_vowels(word):
    has_vowel = False
    for i in range(len(word)):
        if word[i] in vowels:
            has_vowel = True
            break
    return not has_vowel

inp = input("Enter a sentence to huzzify: ")
print(huzzify_sentence(inp))

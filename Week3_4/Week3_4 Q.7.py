def word_frequency(sentence):
    words = sentence.split()
    freq = {}
    for x in words:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    return freq
sentence = input("Enter a sentence: ")
result = word_frequency(sentence)
print("Word frequencies: ", result)

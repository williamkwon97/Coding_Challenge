def reverse(sentence):

    #splitting the sentence into list of words.
    words = sentence.split(" ")

    #reversing each word and creating
    #a new list of words
    #[start:end:step]
    newWords = [word[::-1] for word in words]

    newSentence = " ".join(newWords)

    return newSentence


sentence = "GeeksforGeeks"

print(reverse(sentence))

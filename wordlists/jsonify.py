wordlist = "10k_legal_"

"""
with open(wordlist+".txt") as f:
    output = {}
    for i in range(2,7):
        output[i] = open(wordlist+"_"+str(i)+".txt", "w+")
    count = 0
    for word in f.readlines():
        word = word.strip("\n")
        if 2 <= len(word) <= 6:
            output[len(word)].write(word+"\n")
            if count > 10: break
"""
letter_scores = {
    "E": 1,
    "A": 1,
    "S": 1,
    "R": 1,
    "T": 1,
    "I": 1,
    "N": 1,
    "O": 1,
    "L": 1,
    "D": 1,
    "M": 2,
    "P": 2,
    "G": 2,
    "U": 3,
    "C": 3,
    "B": 3,
    "H": 3,
    "F": 4,
    "W": 4,
    "Y": 4,
    "V": 6,
    "K": 6,
    "X": 8,
    "Z": 8,
    "J": 8,
    "Q": 10,
    }

def word_score(word, score):
    return sum([score[letter] for letter in word])

"""
for i in range(3,7):
    with open(wordlist+str(i)+".txt")
"""


with open("10k_legal.json", "w+") as output:
    output.write("{\n")
    for i in range(3,7):
        with open(wordlist+str(i)+".txt") as input:
            output.write('\t"'+str(i)+'": {\n')
            for word in input.readlines():
                word = word.strip("\n").upper()
                output.write('\t\t"{}": {},\n'.format(word, word_score(word, letter_scores)))
            output.write("\t},\n")
    output.write("}")


"""
for i in range(3,7):
    with open(wordlist+str(i)+".txt") as input:
        with open(wordlist+str(i)+".json", "w+") as output:
            output.write("{\n")
            for word in input.readlines():
                output.write('\t"{}": 1,\n'.format(word.strip("\n")))
            output.write("}")
"""

wordlist = "20k_legal_"

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

with open("20k_legal.json", "w+") as output:
    output.write("{\n")
    for i in range(3,7):
        with open(wordlist+str(i)+".txt") as input:
            output.write('\t{}: ['.format(i))
            for word in input.readlines():
                output.write('"{}", '.format(word.strip("\n")))
            output.write("],\n")
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

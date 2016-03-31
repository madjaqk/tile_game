wordlist = "sowpods"

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
with open(wordlist+".txt") as f:
    with open("sowpods_3.txt", "w") as g:
        for word in f.readlines():
            word = word.strip("\n")
            if len(word) == 3:
                g.write(word+"\n")
                

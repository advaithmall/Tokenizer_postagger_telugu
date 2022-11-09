import stanza
#stanza.download('te')
filename = 'telcorpus.txt'
#print("open")
file = open(filename,'r')

nlp = stanza.Pipeline('te',processors='tokenize,lemma',use_gpu=False)

#print("kesf")
with open("lemma.txt", "w") as out_file:
    for line in file:
        #print("loop1")
        doc = nlp(line)
        for sentence in doc.sentences:
            #print("loop2")
            for word in sentence.words:
                #print("loop3")
                print("word: ",word.text,"lemma: ",word.lemma,file=out_file)
file.close()

import stanza
import pandas as pd
import numpy as np
#stanza.download('te')
filename = 'telcorpus.txt'
#print("open")
file = open(filename,'r')

nlp = stanza.Pipeline('te',processors='tokenize',use_gpu=False)

#print("kesf")
words_f=[]
with open("tel_lemma.txt", "w") as out_file:
    for line in file:
        #print("loop1")
        doc = nlp(line)
        for sentence in doc.sentences:
            #print("loop2")
            for word in sentence.words:
                words_f.append(word.text)
file.close()
df = pd.value_counts(np.array(words_f))
#print(df.to_string())
with open("tel_freq.txt", "a") as o_file:
    #print("Frequency of lemma")
    print(df.to_string(), file=o_file)

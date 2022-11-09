import stanza
#stanza.download('te')
filename = 'telcorpus.txt'
#print("open")
file = open(filename,'r')

nlp = stanza.Pipeline('te',processors='tokenize,pos',use_gpu=False)
with open("tel_tokensw.txt", "w") as out_file:
    for line in file:
        doc = nlp(line)
        #print(*[f'word: {word.text}\tupos: {word.upos}\txpos: {word.xpos}\tfeats: {word.feats if word.feats else "_"}' for sent in doc.sentences for word in sent.words], sep='\n')
        for sentence in doc.sentences:
            #print("loop2")
            output_line=""
            for token in sentence.words:
                #print("entered loop last")
                #output_line+=word.text+"_"+word.pos+" "
                print(token.text,file=out_file)
                #out = token.text
                #print(out)
file.close()

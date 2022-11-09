import stanza
#stanza.download('te')
filename = 'telcorpus1.txt'
#print("open")
file = open(filename,'r')

nlp = stanza.Pipeline('te',processors='tokenize,pos',use_gpu=False)
with open("pos_tags.txt", "w") as out_file:
    for line in file:
        doc = nlp(line)
        #print(*[f'word: {word.text}\tupos: {word.upos}\txpos: {word.xpos}\tfeats: {word.feats if word.feats else "_"}' for sent in doc.sentences for word in sent.words], sep='\n')
        for sentence in doc.sentences:
            output_line=""
            for word in sentence.words:
                output_line+=word.text+"_"+word.pos+" "
            print(output_line,file=out_file)
file.close()

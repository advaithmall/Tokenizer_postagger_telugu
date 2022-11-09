import pprint
words = dict()
filename = 'tel_freq.txt'
#print("open")
file = open(filename,'r')
count =0
for line in file:
    count+=1
    word,freq = line.split()
    words[word]=int(freq)
    if (count>=100):
        break
#pprint.pprint(words)
from matplotlib import pyplot as plt
from matplotlib import font_manager


courses = list(words.keys())
frequencies = list(words.values())
fig = plt.figure(figsize=(10,5))
font_dir = ["./font"]
for font in font_manager.findSystemFonts(font_dir):
    font_manager.fontManager.addfont(font)
plt.rcParams['font.family'] = 'Aller-Bold'
plt.xlabel("Times of appearance")
plt.title('Word Distribution Telugu', size=20)
plt.ylabel("Words in Teelugu")
plt.bar(courses, frequencies, width=0.2)
plt.plot(courses,frequencies)
plt.show()

#%matplotlib inline

import matplotlib
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer,WhitespaceTokenizer
from nltk import corpus
import nltk


#Download and convert it to text
r= requests.get("https://s3.amazonaws.com/assets.datacamp.com/production/project_147/datasets/2701-h.htm")
r.encoding="utf-8"
text=BeautifulSoup(r.text).get_text()

#Use RegexToken to split words
# \W will fit A-Za-z0-9 and underscore
#+ means it can repeat any time possible
tokens = RegexpTokenizer("\w+").tokenize(text)
# We can use WhiteSpaceTokenizer() instead
#tokens2= WhitespaceTokenizer().tokenize(text)

word=[]
for t in tokens:
    word.append(t.lower())

#Create a list of stopword. Auto download to /home/kennyt/nltk_data
nltk.download("stopwords")
sw=corpus.stopwords.words("english")

#Remove stopword
word_ns=[]
for w in word:
    if w not in sw:
        word_ns.append(w)

#Build graph
nltk.FreqDist(word_ns).plot(25)
plt.show()
# print(tokens[:8])
#print(tokens2[:8])
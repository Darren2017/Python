import nltk
from nltk.corpus import stopwords
from collections import Counter
#nltk.download('punkt')
#nltk.download('stopwords')

file = open('/Users/darren/Downloads/data/Obama.txt', 'r', encoding='gbk')
raw_file = file.read()
sens = nltk.sent_tokenize(raw_file)
words = nltk.word_tokenize(raw_file)

stop_words = stopwords.words('english') + [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%','-','--','’','—', "''", '""']
filter_words = [word for word in words if word not in stop_words]

token = Counter(filter_words).most_common(30)
print(token)

freq = nltk.FreqDist(filter_words)
freq.plot(20, cumulative=False)

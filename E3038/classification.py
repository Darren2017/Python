import nltk
import random
import pickle

from nltk.corpus import movie_reviews


#读取数据，并将每一篇文档和对应标签放在一起，一个元祖里面
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
# 将文件打乱顺序
random.shuffle(documents)
all_words = [] #构建词典
for w in movie_reviews.words():
    all_words.append(w.lower())
all_words = nltk.FreqDist(all_words) #每一个单词出现的次数统计
word_features = list(all_words.keys())[:3000]

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

# 打印出特征集
# print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

# 保存特征存在性布尔值，以及它们各自的正面或负面的类别
featuresets = [(find_features(rev), category) for (rev, category) in documents]

# 分割数据
training = featuresets[:1900]
testing = featuresets[1900:]

# 对分类器进行训练
classifier = nltk.NaiveBayesClassifier.train(training)

# 测试的准确率
print("Classifier accuracy percent:", (nltk.classify.accuracy(classifier, testing)))

# 每个词从负面到正面出现的概率
classifier.show_most_informative_features(15)

# 利用nltk保存分类器
save_classifier = open("naivebayes.pickle", "wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

# # 使用分类器
# classifier_f = open("naivebayes.pickle", "rb")
# classifier = pickle.load(classifier_f)
# classifier_f.close()


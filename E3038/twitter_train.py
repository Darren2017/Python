import nltk
import sys
import random
import pickle
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
nltk.download('brown')

def find_features(documents):
    words = word_tokenize(documents)
    features = {}
    for word in train_text_word_features:
        features[word] = (word in words)

    return features


if __name__ == "__main__":

    twitter_message_neg = open("neg.txt", "r").read()
    twitter_message_pos = open("pos.txt", "r").read()

    document = [] #保存文本，元组（句子，标签）

    for word in twitter_message_neg.split('\n'):
        document.append((word, "neg"))

    for word in twitter_message_pos.split('\n'):
        document.append((word, "pos"))

    random.shuffle(document) #随机打乱
    train_text = [] #词典


    twitter_message_pos_words = word_tokenize(twitter_message_pos)#分词
    twitter_message_neg_words = word_tokenize(twitter_message_neg)

    for word in twitter_message_neg_words:
        if word not in stop_words:
            train_text.append(word)
    for word in twitter_message_pos_words:
        if word not in stop_words:
            train_text.append(word)

    train_text = nltk.FreqDist(train_text)XXQ

    train_text_word_features = list(train_text.keys())[:3000]

    featuressets = [(find_features(rev), category) for (rev, category) in document]

    train_text_set = featuressets[:10000]
    test_text_set = featuressets[10000:]

    classifier_f = open("naivebayes.pickle", "rb")
    classifier = pickle.load(classifier_f)
    classifier_f.close()

    classifier = nltk.NaiveBayesClassifier.train(train_text_set)
    print("Original Naive Bayes Algo accuracy percent:", (nltk.classify.accuracy(classifier, test_text_set)) )
    classifier.show_most_informative_features(15)

    # save_classifier = open("naivebayes_twitter_text.pickle", "wb")
    # pickle.dump(classifier, save_classifier)
    # save_classifier.close()



#!/usr/bin/env python
# coding=utf-8

import jieba

def load_stop_word(file):
    stop_words = [line.strip() for line in open(file, 'r').readlines()]
    return stop_words

def cut_sentence(sentence):
    jieba.load_userdict('/Users/darren/Downloads/data/userdict.txt')
    seged_sentence = jieba.cut(sentence, cut_all=True, HMM=True)
    stop_words = load_stop_word('/Users/darren/Downloads/data/chineseStopWords.txt')
    output = ""
    for word in seged_sentence:
        if word not in stop_words:
            if word != '\t':
                output += word
                output += "|"
    return output

if __name__ == '__main__':
    cut_word = ""
    with open('/Users/darren/Downloads/data/test001.txt', 'r') as f:
        for line in f.readlines():
            line_list = line.split()
            real_line = "".join(line_list)
            cut_word += cut_sentence(real_line)
    print(cut_word)

from tkinter import *
import jieba
import nltk
import jieba.posseg as pseg
import collections
import wordcloud
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'SimHei'

class NLP_GUI(Tk):
    def __init__(self):
        self.init_window = Tk()
        self.init_window.title("文本处理工具--唐爱民")
        self.init_window.geometry("1068x681+10+10")

        self.read_label = Label(self.init_window, fg='yellow',bg='blue', text="待处理数据")
        self.read_label.grid(row=0, column=0)
        # self.read_label.pack()
        self.result_label = Label(self.init_window, fg='yellow',bg='blue', text="处理结果")
        self.result_label.grid(row=0, column=12)
        # self.result_label.pack()

        self.read_Text = Text(self.init_window, width=67, height=35)
        self.read_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        # self.read_Text.pack()
        self.result_Text = Text(self.init_window, width=70, height=49)
        self.result_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
        # self.result_Text.pack()

        self.button_fenci_with_stopwords = Button(self.init_window, text = "分词(去停用词)", fg='yellow', bg='blue', width=18,relief=GROOVE, command=self.cut_with_stopwords)
        self.button_lable_with_stopwords = Button(self.init_window, text="词性标注(去停用词)", fg='yellow', bg='blue', width=18, command=self.lable_with_stopwords)
        self.button_fenci_with_stopwords.grid(row=1, column=11)
        self.button_lable_with_stopwords.grid(row=2, column=11)
        self.button_fenci_without_stopwords = Button(self.init_window, text = "分词", fg='yellow', bg='blue', width=18,relief=GROOVE, command=self.cut_without_stopwords)
        self.button_lable_without_stopwords = Button(self.init_window, text="词性标注", fg='yellow', bg='blue', width=18, command=self.lable_without_stopwords)
        self.button_fenci_without_stopwords.grid(row=3, column=11)
        self.button_lable_without_stopwords.grid(row=4, column=11)
        self.button_cipin = Button(self.init_window, text = "词频展示", fg='yellow', bg='blue', width=18,relief=GROOVE, command=self.show_cipin)
        self.button_ciyun = Button(self.init_window, text="词云", fg='yellow', bg='blue', width=18, command=self.show_ciyun)
        self.button_cipin.grid(row=5, column=11)
        self.button_ciyun.grid(row=6, column=11)
        # self.button_fenci.pack()
        # self.button_lable.pack()
        self.init_window.mainloop()

    def load_stop_word(self, file):
        stop_words = [line.strip() for line in open(file, 'r', encoding = 'utf-8').readlines()]
        return stop_words

    def cut_with_stopwords(self):
        jieba.load_userdict('C:\\Users\\data\\userdict.txt')
        stop_words = self.load_stop_word('C:\\Users\\data\\chineseStopWords.txt')
        text = self.read_Text.get(1.0, END).strip().replace('\n', '')
        if text:
            text_list = text.split()
            real_text = "".join(text_list)
            seged_sentence = jieba.cut(real_text, cut_all=False, HMM=True)
            output = ""
            for word in seged_sentence:
                if word not in stop_words:
                    if word != '\t':
                        output += word
                        output += "|"
            self.result_Text.delete(1.0, END)
            try: 
                self.result_Text.insert(1.0, output)
            except:
                pass
    
    def cut_without_stopwords(self):
        jieba.load_userdict('C:\\Users\\data\\userdict.txt')
        text = self.read_Text.get(1.0, END).strip().replace('\n', '')
        if text:
            text_list = text.split()
            real_text = "".join(text_list)
            seged_sentence = jieba.cut(real_text, cut_all=False, HMM=True)
            output = ""
            for word in seged_sentence:
                output += word
                output += "|"
            self.result_Text.delete(1.0, END)
            try: 
                self.result_Text.insert(1.0, output)
            except:
                pass

    def lable_with_stopwords(self):
        stop_words = self.load_stop_word('C:\\Users\\data\\chineseStopWords.txt')
        text = self.read_Text.get(1.0, END).strip().replace('\n', '')
        if text:
            text_list = text.split()
            real_text = "".join(text_list)
            words = pseg.cut(real_text)
            try:
                result = []
                for word, flag in words:
                    if word not in stop_words:
                        if word != '\t':
                            result.extend(word+ "\\"  + flag + "   ")
                result = ''.join(result)
                self.result_Text.delete(1.0,END)
                self.result_Text.insert(1.0,result)
            except:
                self.result_Text.delete(1.0,END)

    def lable_without_stopwords(self):
        text = self.read_Text.get(1.0, END).strip().replace('\n', '')
        if text:
            text_list = text.split()
            real_text = "".join(text_list)
            words = pseg.cut(real_text)
            try:
                result = []
                for word, flag in words:
                    result.extend(word+ "\\"  + flag + "   ")
                result = ''.join(result)
                self.result_Text.delete(1.0,END)
                self.result_Text.insert(1.0,result)
            except:
                self.result_Text.delete(1.0,END)

    def show_cipin(self):
        stop_words = self.load_stop_word('C:\\Users\\data\\chineseStopWords.txt')
        text = self.read_Text.get(1.0, END).strip().replace('\n', '')
        if text:
            text_list = text.split()
            real_text = "".join(text_list)
            seged_sentence = jieba.cut(real_text, cut_all=False, HMM=True)
            real_sentence = [i for i in seged_sentence if i not in stop_words]
            freq = nltk.FreqDist(real_sentence)
            freq.plot(20,cumulative=False)

    def show_ciyun(self):
        stop_words = self.load_stop_word('C:\\Users\\data\\chineseStopWords.txt')
        text = self.read_Text.get(1.0, END).strip().replace('\n', '')
        if text:
            text_list = text.split()
            real_text = "".join(text_list)
            seged_sentence = jieba.cut(real_text, cut_all=False, HMM=True)
            real_sentence = [i for i in seged_sentence if i not in stop_words]
            word_counts = collections.Counter(real_sentence)
            wc = wordcloud.WordCloud(
                font_path='C:\\Users\\data\\SourceHanSans-Bold.ttc',
                max_words=200,
                max_font_size=100)
            wc.generate_from_frequencies(word_counts)
            plt.imshow(wc)
            plt.axis('off')
            plt.show()

nil = NLP_GUI()

import jieba
import os

Pos_find='/Users/darren/Downloads/cut/'    #需要解压缩的目录
Pos_mved="/Users/darren/Downloads/newcut/"  #解压缩之后文件的储存目录

import os
for(dirpath,dirnames,files)in os.walk(Pos_find): #遍历当前目录下的全部文件以及子文件
    for filename in files:
        if filename.split('.')[1] == 'txt':
            print(filename)
            try:
                filepath = os.path.join(dirpath, filename)  #构造当前文件的路径
                # print(filepath)
                # f = open(filepath)
                # content = f.read()
                # print(content)
                with open(filepath) as f:
                    content = f.read()
                    # print(content)
                    newcontent = jieba.cut(content)
                with open(Pos_mved + filename, 'w') as nf:
                    nn = ' '.join(newcontent)
                    nf.write(nn)
                    
            except Exception as e:
                print(e)
                pass
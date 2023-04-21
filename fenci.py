'''
yuxiao 2021/2/5
结巴提取xml名词
'''

#xml文件和隐私政策文件处理代码


import jieba
import jieba.posseg as jb
import jieba.analyse
import re
import os
jieba.load_userdict("I:/IoTSensitiveDataAnalysis/数据/xml信息提取/HuaMiXMLInfo.txt")  #自定义词典

#thu1 = thulac.thulac(seg_only=True)
#thu1.cut_f("I:/IoTSensitiveDataAnalysis/数据/string文件/huami.txt", "I:/IoTSensitiveDataAnalysis/数据/string文件/thulacmark/huami.txt")

#提取中文信息
#提取xml中><间的内容

path = "I:/IoTSensitiveDataAnalysis/数据/xml文件/标签提取/" #待分词标记的原始文本
aftermarkfi = "I:/IoTSensitiveDataAnalysis/数据/xml文件/jiebamark/"  #经过结巴分词标记的文本
nlist = "I:/IoTSensitiveDataAnalysis/数据/xml文件/标签提取/jbxmlsum.txt"


# 结巴分词文本逐句标记
n = []
files = os.listdir(path)

for file in files:
    if file.endswith(".txt"):
        fi = path+file
        with open(fi, encoding='utf-8')as f:
            print("开始处理：", fi)
            for line in f.readlines():
                print("标记前:", line)
                biaoji = jb.cut(line)  # True为全模式 False精确模式，默认精确模式
                sl = ''
                for word, flag in biaoji:
                    s = word + '/' + flag
                    sl += s
                    if flag == 'n':
                        print("名词：", word)
                        if word not in n:
                            n.append(word)  # 提取名词列表
                            with open(nlist, 'a', encoding='utf-8')as nl:
                                nl.write(word + '\n')

                print("标记后:", sl)

                with open(aftermarkfi+file, 'a', encoding='utf-8')as fi:
                    fi.write(sl)


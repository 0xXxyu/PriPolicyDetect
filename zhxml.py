xmlfile = "I:/IoTSensitiveDataAnalysis/数据/xml文件/midjk.txt"
file = ""

'''
提取标签内容并进行词性标记
'''

#提取xml文件标签内容
with open(xmlfile, encoding='utf-8')as f:
    for line in f.readlines():
        # print(line)
        try:
            lin = line.split('<', 2)[1]
            li = lin.split('>')[1]
            with open(file, 'a', encoding='utf-8') as biaoj:
                biaoj.write(li+'\n')
            print("标记前：", li)
            #biaoji = jb.cut(li)
            #print(biaoji)
            # for word, flag in biaoji:
                #print(word)
            # print(li)
        except:
            break
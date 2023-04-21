import re
import os

#提取标记后的名词
dir = "I:/IoTSensitiveDataAnalysis/数据/xml信息提取/output/"
files = os.listdir(dir)

savefl = "I:/IoTSensitiveDataAnalysis/数据/xml信息提取/sum.txt"
lis = [] #列表用来去重


for file in files:
    fi = dir+file
    with open(fi, encoding='utf-8')as f:
        print("开始处理：", fi)
        for line in f.readlines():
            # print(line)
            t = re.findall(' [a-zA-Z\u4e00-\u9fa5]*/n|[a-zA-Z\u4e00-\u9fa5]*/n', line)
            # print('名词提取：', t)
            if t == None:
                break
            else:
                for value in t:
                    n = value.split('/n')[0].replace(' ', '')
                    if n not in lis:
                        lis.append(n)
                        # with open(savefl, 'a')as sf:
                            # sf.write(n + '\n')
                    else:
                        break
                    #print('最终：', n)
print(lis)



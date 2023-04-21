import nltk
import re
from ENCiPro import Cipro
from ReadList import ReadList
import os


sumsenlist = ReadList.readlist('./data/enSenSum.txt')
sumsen = sumsenlist[0].split(', ')              #敏感信息词汇列表
senslist = {}
for sens in sumsen:
    sen = sens.replace(' ', '').lower()
    senslist[sen] = sens
print(senslist)


addlist = ReadList.readlist('./data/EnAddDict.txt')
add = dict(x.split("|||") for x in addlist[0].split(', '))          #敏感信息映射词典
#print(add.keys())

keydir = "I:/IoTSensitiveDataAnalysis/数据/设备抓包/Keyv23/小米colorv23.txt"
keylist = ReadList.readlist(keydir)
keylis = ''.join(keylist).split('\n')       #keys
print("key列表：", keylis)

enpath = "I:/IoTSensitiveDataAnalysis/数据/设备抓包/ENKeySen/小米colorv23.txt"
keysenlist = []

#拆分组合的key
def chaifen(key, type):
    try:
        if type == 1:  # 大写字母分割
            sl = re.findall('[A-Z][a-z]*', key)
            print("sl:", sl)
            sa = []
            for sln in sl:
                sln1 = sln.lower()
                sa.append(Cipro.lemmatize_sentence(sln1))
                print("sln:", sln)
                z = type.split(sln)
                print("z:", z)
                for zl in z:
                    if zl not in sa:
                        if zl == '':
                            print("null")
                        else:
                            print("添加前：", sa)
                            zl = zl.lower()
                            sa.append(Cipro.lemmatize_sentence(zl))
                            print("添加：", sa)
            print(sa)
            return sa
        elif type == 0:
            sl = key.split('_')
            # print("sl:", sl)
            sa = []
            for sln in sl:
                if sln.lower() not in sa:
                    sln1 = sln.lower()
                    sa.append(Cipro.lemmatize_sentence(sln1))
                print("sln:", sln)
                z = key.split(sln)
                print("z:", z)
                for zl in z:
                    if zl not in sa:
                        if zl == '':
                            print("null")
                        else:
                            print("添加前：", sa)
                            zl = zl.lower().replace('_', '')
                            sa.append(Cipro.lemmatize_sentence(zl))
                            print("添加：", zl)
            return sa
    except:
        print("key非字母非拼接：", key)


#判断key是否在senslist中
def keyifsen(key):
    if key in senslist:
        if key not in keysenlist:
            keysenlist.append(key)
        return 1

#判断拆分后重组的列表中是否匹配到敏感信息
def keyaferchai(keychailist):
    # print("拆分后列表：", keychailist)
    try:
        for keychai in keychailist:
            if keychai in add.keys():
                print("拆分后存在于敏感词典：", add[keychai])
                value = add[keychai]
                if value in senslist.keys():
                    keysenlist.append(value)
                    break
            else:
                flag = keyifsen(keychai)
                if flag == 1:
                    break
    except:
        print("key 为空或不能处理：", keychailist)


for k in keylis:
    print("开始处理：", k)
    ke = Cipro.lemmatize_sentence(k)
    key = ke[0]
    if key.lower() in senslist.keys():                        #key直接为敏感词汇
        print("key为敏感信息：", key)
        if key.lower() not in keysenlist:
            keysenlist.append(senslist[key.lower()])
            print("1敏感信息：", senslist[key.lower()])

    elif key in add.keys():  # 直接是添加的敏感映射
        print("key在敏感信息映射字典中：", key)
        value = add[key]
        if value.replace(' ', '') in senslist.keys():
            print("存在于敏感词典：", value)
            keysenlist.append(value)
            print("2敏感信息：", value)

    else:
        print("尝试分割：", key)
        if re.findall('_', key):    #处理下划线分割
            print("key为_拼接：", key)
            keyafter = chaifen(key, 0)          #下划线拆分,拆分后返回小写列表
            print("key拆分后：", keyafter)
            keyaferchai(keyafter)               #拆分重组后依次判断是否敏感

        else:
            print("key为大写")
            keychailist = chaifen(key, 1)     #大写拆分
            keyaferchai(keychailist)

ReadList.writelist(keysenlist, enpath)
print(keysenlist)



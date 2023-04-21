import jieba
import jieba.posseg as jb
import jieba.analyse
from urllib import parse
from ReadList import ReadList
from KeyTran import KeyfTran
from KeyForSen import Tran

s = u"最高血压"
print(type(s))
c = jb.cut(s)
#print(' '.join(c))
n = []
for sl, flag in c:
    cs = sl+'/'+flag
    n.append(cs)
print(''.join(n))


'''
str = "{'ssss': 'data_hr','data_json': '%5B%7B%22data_hr'}"
str2 = parse.unquote(str)
print(str2)
'''

'''
#lis = []
fi = "./data/SenSum.txt"
sumsen = ReadList.readlist(fi)
sumseli = sumsen[0].split('、')

keysendir = "I:/IoTSensitiveDataAnalysis/数据/设备抓包/KeyAfterTranv23/wofitsumv23.txt"
sen = ReadList.readlist(keysendir)
keytranli = ''.join(sen).split('\n')

print(sumseli)
# print(len(keytranli))

senlist = Tran.ifSen(sumseli,keytranli)
print(len(keytranli))
'''

'''
s = ['设备ID', '用户ID', '生日', '性别', '设备名称', '血氧饱和度', '设备MAC', '位置']
#s = '1234d
print(str(s))
'''

'''
path = "./data/xmlSenSum.txt"
senlist = ReadList.readlist(path)
sen1 = ''.join(senlist).split('\n')
print("xmlsensum：", sen1)

path2 = "./data/SenSum.txt"
senlis = ReadList.readlist(path2)
sen2 = ''.join(senlis).split('、')
print("sensum：", sen2)


sen3 = sen2
for sen in sen1:
    if sen not in sen2:
        sen3.append(sen)
    else:
        print("存在！")
ReadList.writelist(sen3, './data/SenSum1.txt')
'''

'''
path = "I:/IoTSensitiveDataAnalysis/数据/设备抓包/Keyv23/honor 5i.txt"
aftertxt = "I:/IoTSensitiveDataAnalysis/数据/设备抓包/KeyAfterTranv23/honor 5iv24.txt"
sumtxt = "I:/IoTSensitiveDataAnalysis/数据/设备抓包/KeyAndTran/honor 5iv24.txt"

KeyfTran.keyTran(path,aftertxt, sumtxt)
'''
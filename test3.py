import re
from ReadList import ReadList
from SearchPolicy import Policy
import nltk
from KeyForSen import Tran
import jieba
from ENCiPro import Cipro
'''
组合单词和下划线单词
'''
'''
s = "min_Stress_Avg"
sl = s.split('_')
#sa = sl
#sl = re.findall('[A-Z][a-z]*', s)
print("sl:",sl)
sa = []
for sln in sl:
    if sln.lower() not in sa:
        sa.append(sln.lower())
    print("sln:",sln)
    z = s.split(sln)
    print("z:",z)
    for zl in z:
        if zl not in sa:
            if zl == '':
                print("null")
            else:
                print("添加前：", sa)
                zl =zl.lower().replace('_','')
                sa.append(zl)
                print("添加：", zl)
print(sa)
'''

'''
sens = ReadList.readlist('./data/SenSum.txt')
sen = sens[0].split('、')
print(len(sen))
s = []
for se in sen:
    if se not in s:
        s.append(se)
    else:
        print(se)
print(s)
print(len(s))
'''

'''
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None


def lemmatize_sentence(sentence):
    res = []
    lemmatizer = WordNetLemmatizer()
    for word, pos in pos_tag(word_tokenize(sentence)):
        wordnet_pos = get_wordnet_pos(pos) or wordnet.NOUN
        res.append(lemmatizer.lemmatize(word, pos=wordnet_pos))

    return res

se = 'steps'
re = lemmatize_sentence(se)
print(re)
'''
'''
senpath = "I:/IoTSensitiveDataAnalysis/数据/设备抓包/ENKeySen/honor5i.txt"
respath = "I:/IoTSensitiveDataAnalysis/数据/ENRes/honor5i.txt"

senlist = ReadList.readlist(senpath)
sens = ''.join(senlist).split('、')
print(sens)
polciydir = "I:/IoTSensitiveDataAnalysis/数据/隐私政策en/huawei health.txt"

Policy.whatlist(sens, polciydir,respath)
'''

'''
#nltk分词
s = "Xiao Ming graduated from Tsinghua University in Beijing."
t = nltk.word_tokenize(s)
p = nltk.pos_tag(t)
print('/'.join(t))
p0 = ''
for pi in p:
    pr = pi[0]+'/'+pi[1]+' '
    p0 = p0+pr
print(p0)
'''
'''
# 评估敏感信息检测
sumlist = ReadList.readlist("./data/SenSum.txt")
sum = sumlist[0].split('、')

senlist = ReadList.readlist("I:/IoTSensitiveDataAnalysis/数据/设备抓包/KeyAfterTranv23/SamsungSumv23.txt")
sen = ''.join(senlist).split('\n')
print("总信息数量：", len(sen))
li = Tran.ifSen(sum,sen)
'''

s = "Xiao Ming graduated from Tsinghua University in Beijing."
sl = Cipro.lemmatize_sentence(s)
print(' '.join(sl))

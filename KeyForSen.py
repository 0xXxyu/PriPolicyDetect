'''
2021/02/07
提取实际通信过程中的敏感信息
'''

import jieba
import jieba.posseg as jb
import jieba.analyse
from KeyTran import KeyfTran
jieba.load_userdict("I:/IoTSensitiveDataAnalysis/数据/xml信息提取/HuaMiXMLInfo.txt")  #敏感信息字典


class Tran:
    feimin = 0
    #读取文件
    # senKeyli = []     #单独运行该函数这么写
    def readsumsen(path):
        with open(path, 'r', encoding='utf-8-sig')as senf:
            sens = senf.readlines()
            senf.close()
            return sens

    def keyifinsum(key, sumsenlist):

        if key in sumsenlist:
            Tran.feimin += 1
            print("key虽然不存在，但其中存在：", key)
            return key
        else:
            return None


    def ifSen(sumsenlist, keylist):

        senKeyli = []       #函数调用这么写
        for key in keylist:
            print("开始分类key：", key)
            if key in sumsenlist:
                Tran.feimin+=1
                print("扫描到敏感信息：", key)
                if key not in senKeyli:
                    senKeyli.append(key)
            else:
                nkey = jb.cut(key)
                # print("jb处理后：", nkey)
                for word,flag in nkey:
                    if flag=='n':
                        print("可以分割：", word)
                        res = Tran.keyifinsum(word, sumsenlist)
                        if res not in senKeyli and res != None:
                            senKeyli.append(res)
                            print("分割后：", res)
        print("被分为敏感信息的数量：")
        print(Tran.feimin)
        return senKeyli


if __name__=="__main__":

    keylistpath = "I:/IoTSensitiveDataAnalysis/数据/设备抓包/KeyAfterTranv23/wofitsumv23.txt"       #翻译后数据
    Sensumpath = "./data/SenSum.txt"                                                     #敏感信息库
    keylist = Tran.readsumsen(keylistpath)
    #keyspath = "I:/IoTSensitiveDataAnalysis/数据/设备抓包/Key提取截取方式/HonorSum.txt"           #待翻译的key
    # keylist = KeyfTran.keyTran(keyspath)  # 调用keytran翻译，数据包中包含的敏感信息



    keyli = []
    sumsenlist = Tran.readsumsen(Sensumpath)
    sumli = []
    for key in keylist:
        key = key.strip('\n')
        keyli.append(key)
    for key in sumsenlist:
        key = key.strip('\n')
        sumli.append(key)
    print("sum:",sumli)
    print("key len", len(keyli))

    senli,feimin = Tran.ifSen(sumli, keyli)    # key代表的信息是否包含在敏感列表，给出在敏感信息列表的
    print(senli,feimin)

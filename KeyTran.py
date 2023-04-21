'''
yu 2021/02/08
实现key到目标语言的转换
'''

from BaiduTrans import BaiduTrans   #百度翻译api
from bingTran import BingTrans  #bing翻译api
import os
import re
from ReadList import ReadList

# path = "I:/IoTSensitiveDataAnalysis/数据/设备抓包/Key提取截取方式/"
aftertrapath = "I:/IoTSensitiveDataAnalysis/数据/设备抓包/KeyTran/"    #翻译结果保存
# keyandtran = "I:/IoTSensitiveDataAnalysis/数据/设备抓包/KeyAndTran/"   #翻译和翻译前保存
'''
#处理大量数据时
keytxts = os.listdir(path)
        for keytxt in keytxts:
            txt = path + keytxt
'''

class KeyfTran:

    def keyTran(path, aftertxt, sumtxt):
        addsenpath = "./data/TranAddDict.txt"
        addsenlist = ReadList.readlist(addsenpath)  # 读取翻译的手工添加字典
        senstr = ''.join(addsenlist)
        addsens = dict(x.split("|||") for x in senstr.split('、'))  # {"timezone":"时区"}  #把txt写到字典里
        print(addsens)

        aftertra = []
        sumlist = []
        #aftertxt = aftertrapath + 'opposumv23.txt'                           #翻译结果修改！！！！！！！！！
        # sumtxt = keyandtran+keytxt

        with open(path, 'r', encoding='utf-8') as keytx:
            print("开始处理：", path)
            keys = keytx.readlines()

            for key in keys:
                ke = key.replace('\n', '')
                print("开始翻译：", ke)
                #ke1list = re.findall(r'[A-Z][^A-Z]*', ke)
                #ke2list = re.findall(r'^[a-z]*', ke)
                '''
                #rs = BingTrans.tran(key)
                rs = BaiduTrans.tran(key)
                if rs != key:
                    tra = rs['trans_result'][0]['dst']  #百度翻译
                    # aftertra.append(rs)  # key翻译结果
                    sum = key.replace('\n', '') + "|||" + tra
                    sumlist.append(sum)  # key翻译前后保存到一个list
                    print("翻译结果：", tra)

                else:
                    aftertra.append(key)
                    sum = key.replace('\n', '') + "|||" + key
                    sumlist.append(sum)
                    print("没翻译：", key)

                #处理同厂商设备
                '''
                if ke in addsens.keys():
                    print("字典翻译：", ke)
                    aftertra.append(addsens[ke])
                    print("字典翻译成功，写入:", addsens[ke])
                    sum = ke + "|||" + addsens[ke]
                    sumlist.append(sum)
                else:
                    rs = BaiduTrans.tran(ke)    #调用翻译API出错时返回原词
                    if rs != ke:
                        tra = rs['trans_result'][0]['dst']  #百度翻译
                        aftertra.append(tra)  # key翻译结果
                        sum = key.replace('\n', '') + "|||" + tra
                        sumlist.append(sum)  # key翻译前后保存到一个list
                        print("翻译结果：", tra)

                    else:
                        aftertra.append(ke)
                        sum = ke.replace('\n', '')+"|||"+ke
                        sumlist.append(sum)
                        print("没翻译：", ke)
                    # print(rs)

        #翻译结果
        with open(aftertxt, 'w', encoding='utf-8')as tra:
            for key in aftertra:
                tra.write(key+'\n')

        print(' '.join(sumlist))

        #返回翻译后的列表
        #sumtxt = "I:/IoTSensitiveDataAnalysis/数据/设备抓包/KeyAndTran/opposumv23.txt"  # 修改！！！！
        # sumlist
        with open(sumtxt, 'w', encoding='utf-8')as tra:
            for sum in sumlist:
                #print("sumlist列表：", sum)
                tra.write(sum+'\n')

        return aftertra

from ReadList import ReadList
from KeyTran import KeyfTran
from KeyForSen import Tran
from ENCiPro import Cipro
import re


class Policy:

    def whatlist(senli, policypath, repath):
        policys = ReadList.readlist(policypath)

        share = ['disclose', 'distribute', 'exchange', 'give', 'provide', 'rent', 'report', 'sell', 'send', 'share', 'trade', 'transfer', 'transmit']
        collect = ['access', 'check', 'collect', 'gather', 'know', 'obtain', 'receive', 'save', 'store', 'use']

        for poli in policys:
            #print(policy)
            polic = Cipro.lemmatize_sentence(poli)
            policy = ' '.join(polic)
            print(policy)
            for sen in senli:
                print("开始扫描：", sen)
                sen = sen.lower()
                if re.findall(sen, policy):
                    print('-----------------------------------')
                    print("检测到：", sen)
                    print("检测到的声明句子：", policy)
                    ReadList.writestr("该敏感信息存在声明：" + sen + ' ', repath)
                    ReadList.writestr('\n', repath)
                    ReadList.writestr("声明句子：" + policy+'\n', repath)

                    for shar in share:
                        if re.findall(shar, policy):
                            print('分享声明：', shar)
                            ReadList.writestr("分享声明：" + shar + '\n', repath)
                    for coll in collect:
                        if re.findall(coll, policy):
                            print('收集声明：', coll)
                            ReadList.writestr("收集声明：" + coll + '\n', repath)
                    ReadList.writestr("________________________________"+'\n', repath)





    def senPol(senli, policypath, repath):
        policys = ReadList.readlist(policypath)  # 隐私政策按句保存到list里
        '''
                                                         #敏感信息库
        keyspath = "I:/IoTSensitiveDataAnalysis/数据/设备抓包/Key提取截取方式/huamisum.txt"           #待翻译的key
        keylist = KeyfTran.keyTran(keyspath)  # 翻译
        # keylist = ReadList.readlist(keyspath)
        keyli = []

        Sensumpath = "./data/xmlSenSum.txt"
        sumsenlist = ReadList.readlist(Sensumpath)   #读取定义的敏感信息列表
        sumli = []

        for key in keylist:
            key = key.strip('\n')
            keyli.append(key)
        for key in sumsenlist:
            key = key.strip('\n')
            sumli.append(key)
        print("定义的敏感信息列表:",sumli)
        print("翻译后keylist:", keyli)

        senli = Tran.ifSen(sumli, keyli)    # key代表的信息是否包含在敏感列表，给出在敏感信息列表的
        print(keyspath+"包含的敏感信息："+"\n"+' '.join(senli)+'\n'+'---------------------------------------')
        '''
        shoujili = ['披露','分发','交换','给予','提供','出租','报告','出售','发送','共享','交易','转让','传输']
        chuanli = ['访问','检查','收集','了解','获取','接收','保存','储存','使用','记录']

        for policy in policys:
            # print(policy)
            for sen in senli:
                if re.findall(sen, policy):
                    print('-----------------------------------')
                    print("检测到：", sen)
                    print("检测到的声明句子：", policy)
                    ReadList.writestr("该敏感信息存在声明："+sen + ' ', repath)
                    ReadList.writestr('\n', repath)
                    ReadList.writestr("声明句子："+policy, repath)

                    '''
                    for shouji in shoujili:
                        if re.findall(shouji, policy):
                            print("该句是 "+ shouji + "声明")
                    '''








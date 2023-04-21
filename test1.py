from KeyTran import KeyfTran
import re
from bingTran import BingTrans
from ReadList import ReadList
from KeyPro import KeyPro
import urllib
from KeyForSen import Tran
from SearchPolicy import Policy
import os

#path = "I:/IoTSensitiveDataAnalysis/数据/设备抓包/Key提取截取方式/huamisum.txt"
#li = KeyfTran.keyTran(path)

'''
#提取raw里key值
txtfile = "I:/IoTSensitiveDataAnalysis/数据/设备抓包/orisaz/小米color/raw/"

with open(txtfile, 'r', encoding='UTF-8', errors="replace") as f:
    cont = f.readlines()
    print(cont[0])
    KeyPro.getUrlVal(cont, txtfile)
    KeyPro.allKey(cont, txtfile)

'''
#翻译key


keydir = "I:/IoTSensitiveDataAnalysis/数据/设备抓包/Keyv23/"    #key目录
sumtxt = "I:/IoTSensitiveDataAnalysis/数据/设备抓包/KeyAndTran/"      #key翻译后保存目录
afterdir = "I:/IoTSensitiveDataAnalysis/数据/设备抓包/KeyAfterTranv23/"   #key翻译后保存目录

senkeypath = "I:/IoTSensitiveDataAnalysis/数据/设备抓包/SenKey/"        #key中敏感信息保存目录
policydir = "I:/IoTSensitiveDataAnalysis/数据/隐私政策v23/"
redir = "I:/IoTSensitiveDataAnalysis/数据/结果v24/"

###敏感信息列表####
sens = ReadList.readlist('./data/SenSum.txt')
senslist = ''.join(sens).split('、')
##################
txtnames = os.listdir(keydir)

for txtname in txtnames:
    path = keydir+txtname                   #key文件
    after = afterdir+txtname                #最小压力保存文件
    sum = sumtxt+txtname                       #minStress|||最小压力保存文件
    senkey = senkeypath+txtname              #key中敏感词保存文件
    policypath = policydir+txtname           #隐私政策文件
    repath = redir+txtname                    #隐私政策声明检测结果文件

    keyTranlist = KeyfTran.keyTran(path,after,sum)
    res = Tran.ifSen(senslist, keyTranlist)

    ReadList.writestr('、'.join(res), senkey)                #把检查到的敏感信息写到txt文本
    ReadList.writestr(str(res), senkey)                      #列表格式
    # print(res)

    Policy.senPol(res, policypath, repath)

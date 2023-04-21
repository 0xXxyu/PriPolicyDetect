'''
实现对key的处理
1.翻译遍历xml敏感信息sum
2.剩下的添加手工字典处理
'''

import re
import os
import sys
from urllib import parse
sys.setrecursionlimit(100)

class KeyPro:
    keyli = []

    def getTxt(path):
        files = os.listdir(path)
        for f in files:
            # print("f:", f)
            if f.endswith("_c.txt"):  # 所有发送包
                fi = path + f
                with open(fi, 'r', encoding='UTF-8-sig', errors="replace") as f:
                    print("开始处理：", fi)
                    cont = f.readlines()
                    KeyPro.getUrlVal(cont, fi)  # 提取url params
                    print('______________________________________________')
                      # 提取body keys

    def getUrlVal(cont, fi):

            # print(cont)
            # url = cont[0].split('?')[0].split(' ')[1]
            #GetHTTPS.wSum(url)
            # raw = GetHTTPS.getRaw(cont)
            cons = '||'.join(cont)
            if "Referer" in cons:
                print("url反射")
                url = cons.split('Referer')[1].split('||')[0].replace(': ', '')
                if '?' in url:
                    params = url.split('?')[1].split(' ')[0]
                    #GetHTTPS.wSum(params)  #获取params
                    paramlis = params
                    for x in params.split("&"):
                        if x != '':
                            di = x.split("=")  # 列表['firmware', '6.0.1']，第一个值为key
                            di[0] = parse.unquote(di[0])
                            if di[0] not in KeyPro.keyli:
                                KeyPro.keyli.append(di[0])
                                print("url添加：", di[0])
            else:
                url = cont[0].split('?')[0].split(' ')[1]
                print("url为：", url)
                if '?' in cont[0]:
                    params = cont[0].split('?')[1].split(' ')[0]
                    #GetHTTPS.wSum(params)  #获取params
                    paramlis = params
                    for x in params.split("&"):
                        if x != '':
                            di = x.split("=")  # 列表['firmware', '6.0.1']，第一个值为key
                            di[0] = parse.unquote(di[0])
                            if di[0] not in KeyPro.keyli:
                                KeyPro.keyli.append(di[0])
                                print("url添加：", di[0])
            KeyPro.allKey(cont, fi)

    def allKey(cont, fi):
        if '\n' in cont and cont.index('\n') + 1 < len(cont):
            raw = cont[cont.index('\n') + 1]
            print("初始raw:", raw)
            # print(eval(raw))
            # print(type(raw))
            raw = parse.unquote(raw)
            try:
                ra = eval(raw)
                KeyPro.get_RAWallkey(ra, fi)
            except:
                if 'application/x-www-form-urlencoded' in ''.join(cont):
                    try:
                        for x in raw.split("&"):
                            if x != '':
                                d = x.split("=")  # 列表['firmware', '6.0.1']，第一个值为key
                                if d[0] not in KeyPro.keyli:
                                    KeyPro.keyli.append(d[0])
                                    print("d0添加了！！", d[0])
                    except:
                        print("上传数据为空或为加密数据：", fi)
                elif '{' in ''.join(cont):
                    KeyPro.get_RAWallkey(raw, fi)
                else:
                    print("文件有超出处理范围的数据：", fi)
            '''
            if "application/json" in ''.join(cont):  # json格式
                # raw = eval(repr(raw).replace('\\', ''))
                # print("2:", raw)
                try:
                    KeyPro.get_RAWallkey(raw, fi)
                except:
                    print("文件有超出处理范围的数据：", fi)

            elif 'application/x-www-form-urlencoded' in ''.join(cont):
                try:
                    for x in raw.split("&"):
                        if x != '':
                            d = x.split("=")  # 列表['firmware', '6.0.1']，第一个值为key
                            if d[0] not in KeyPro.keyli:
                                KeyPro.keyli.append(d[0])
                except:
                    print("上传数据为空或为加密数据：", fi)
            #else:
                # print("上传数据为空或为加密数据：", fi)
            '''

    def get_RAWallkey(raw, fi):
        '''
        if dict(x.split("=") for x in raw.split("&")):
            di = dict(x.split("=") for x in raw.split("&"))
            for key in di:
                if key not in KeyPro.keyli:
                    KeyPro.keyli.append(key)'''
        print("get_raw:", raw)
        # print(type(raw))
        raw = str(raw)
        try:
            for x in raw.split("\":"):
                for y in x.split("\':"):
                    # yl.append(y)
                    print("y:", y)
                    z = re.findall(r"(\w*)$", y)[0]
                    print("提取所有\":前key值:", z)
                    if z not in KeyPro.keyli:
                        KeyPro.keyli.append(z)
        except:
            print("字典格式的key提取出错：", fi)
        '''
        if isinstance(raw, dict):
            for x in range(len(raw)):
                temp_key = list(raw.keys())[x]
                #print("key循环：", temp_key)
                if temp_key not in KeyPro.keyli:
                    KeyPro.keyli.append(temp_key)
                    # print("1出添加：", temp_key)

                # print("1列表写入：", temp_key)
                temp_value = raw[temp_key]
                print(temp_value)
                print(type(temp_value))
                #print(eval(temp_value))
                #print(type(eval(temp_value)))
                try:
                    va = eval(temp_value)
                    print("1---value可以eval，从1进入2----")
                    KeyPro.get_RAWallkey(va, fi)
                except:
                    if isinstance(temp_value, (dict, list)):
                        print("------value为字典或列表，从1进入1自我调用-------")
                        KeyPro.get_RAWallkey(temp_value, fi)
                    else:
                        print("--value非dict/list且无法eval：", eval(temp_value))

        elif isinstance(raw, list):
            for k in raw:
                if isinstance(k, dict):
                    for x in range(len(k)):
                        temp_key = list(k.keys())[x]
                        temp_value = k[temp_key]
                        print("list:", temp_value)
                        try:
                            va = eval(temp_value)
                            KeyPro.get_RAWallkey(va, fi)
                        except:
                            if isinstance(temp_value, (dict, list)):
                                KeyPro.get_RAWallkey(temp_value, fi)
                        # if temp_key not in KeyPro.keyli:
                            # KeyPro.keyli.append(temp_key)
                        # print("列表格式写入的key值：", temp_key)

        elif isinstance(eval(raw), dict):
            # print("2 -------进入eval（raw）----------")
            r = eval(raw)
            #print("2 eval 处理value：", type(r))
            for x in range(len(r)):
                temp_key = list(r.keys())[x]
                if temp_key not in KeyPro.keyli:
                    KeyPro.keyli.append(temp_key)
                    #print("2 eval 写入的key：", temp_key)
                # print(KeyPro.keyli)
                temp_value = r[temp_key]
                #print("2eval处理为dic value:", temp_value)
                #print("2 value type:", type(temp_value))
                #print("2 value eval:", eval(temp_value))

                try:
                    va = eval(temp_value)
                    # print("2---value可以eval，从2进入2----")
                    KeyPro.get_RAWallkey(va, fi)
                except:
                    if isinstance(temp_value, (dict, list)):
                        # print("------value为字典或列表，从2进入1自我调用-------")
                        KeyPro.get_RAWallkey(temp_value, fi)
                    #else:
                        #print("2 ----value为字符串")

        elif isinstance(eval(raw), list):
            for k in raw:
                if isinstance(k, dict):
                    for x in range(len(k)):
                        temp_key = list(k.keys())[x]
                        temp_value = k[temp_key]
                        try:
                            va = eval(temp_value)
                            KeyPro.get_RAWallkey(va, fi)
                        except:
                            if isinstance(temp_value, (dict, list)):
                                KeyPro.get_RAWallkey(temp_value, fi)
        else:
            print("该文件存在无法处理数据：", fi)
        '''



if __name__ == "__main__":


    path = "I:/IoTSensitiveDataAnalysis/数据/设备抓包/orisaz/honor 5i/raw/"      #
    keypath = "I:/IoTSensitiveDataAnalysis/数据/设备抓包/Keyv23/honor 5i.txt"

    # keyl = []

    '''
    for fil in files:
        file = path+fil+"/raw/"
        # print(file)
        #keypath = keylist + fil + '.txt'
        print("开始处理：", fil)
        rawdir = os.listdir(file)
    '''

    KeyPro.getTxt(path)
    
    print("总key：", KeyPro.keyli)
    print(len(KeyPro.keyli))

    with open(keypath, 'a', encoding='utf-8')as fk:  # url后的key提取
        for key in KeyPro.keyli:
            fk.write(key + '\n')

    '''
    # fi = "021"
    # r = '{"details":"{"v":"3","phone":"{"brand":"google","model":"Pixel","osversion":"7.1.2","systemtype":"","country":"CN","language":"zh_CN_#Hans","network":"WIFI","resolution":"1794x1080"}","app":"{"appversion":"3.4.7","channel":"a200900101003"}"}","mobileDeviceId":"android_phone"}'
    di = "I:/IoTSensitiveDataAnalysis/数据/设备抓包/orisaz/huamisum/raw/039_c.txt"
    testli = KeyPro.allKey(di)
    # KeyPro.get_RAWallkey(eval(r), fi)
    print(testli)
    '''












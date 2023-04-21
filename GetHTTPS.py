'''
yu 2021/2/5
抓取数据包saz，改后缀为zip解压，raw为发送接收的https数据包
提取其中_c.txt结尾的发送的数据包内容
'''


import os
from urllib.parse import unquote
# from GetRespon import GetRespon

class GetHTTPS:
    inftab = []
    li = []

    #读取saz压缩文件
    def getTxt(path):
        files = os.listdir(path)
        for file in files:
            if file.endswith("_c.txt"):  #所有发送包
                fi = path + file
                # GetHTTPS.getRaw(fi)
                GetHTTPS.getUrlVal(fi)
            #elif file.endswith("_s.txt"):  #所有接收包
                #fi = path + file
                #GetRespon.getRaw(fi)

    #分析url
    def getUrlVal(txtfile):
        with open(txtfile, 'r', encoding='UTF-8', errors="replace") as f:
            cont = f.readlines()
            # print(cont)
            # url = cont[0].split('?')[0].split(' ')[1]
            #GetHTTPS.wSum(url)
            # raw = GetHTTPS.getRaw(cont)
            cons = '||'.join(cont)
            if "Referer" in cons:
                url = cons.split('Referer')[1].split('||')[0].replace(': ', '')
                if '?' in url:
                    params = url.split('?')[1].split(' ')[0]
                    #GetHTTPS.wSum(params)  #获取params
                    paramlis = params
                    for x in params.split("&"):
                        if x != '':
                            di = x.split("=")  # 列表['firmware', '6.0.1']，第一个值为key
                            if di[0] not in GetHTTPS.inftab:
                                GetHTTPS.inftab.append(di[0])
            else:
                url = cont[0].split('?')[0].split(' ')[1]
                if '?' in url:
                    params = url.split('?')[1].split(' ')[0]
                    #GetHTTPS.wSum(params)  #获取params
                    paramlis = params
                    for x in params.split("&"):
                        if x != '':
                            di = x.split("=")  # 列表['firmware', '6.0.1']，第一个值为key
                            if di[0] not in GetHTTPS.inftab:
                                GetHTTPS.inftab.append(di[0])


            #GetHTTPS.wSum(str(raw))
            #GetHTTPS.wSum('-----------------------------------------------------------')



    def getRaw(cont):          #获取txt文件里空行后的数据（准确的前提是过滤无关数据包）
                if cont[0].startswith('POST') or cont[0].startswith('PUT'): #post,get的boby
                    # lis = list(filter(None, lis))  # 去除文件最后的空字符
                    # print("post确认！")
                    if '\n' in cont and cont.index('\n') + 1 < len(cont):
                        raw = cont[cont.index('\n') + 1]
                        # print("cont0:", cont[0])
                        # print('raw: ', type(raw))

                        # print("inf:", type(inf), inf)
                        if "application/json" in ''.join(cont):  # json格式
                            try:
                                dic = eval(raw)
                                print('json:', dic)
                                for key in dic:
                                    GetHTTPS.inftab.append(str(key))
                                    print('tab', GetHTTPS.inftab)
                                return raw
                            except:
                                return raw
                            # print(GetHTTPS.li)
                            # elif inf == None:
                            # GetHTTPS.li.append("null")
                        elif 'application/x-www-form-urlencoded' in ''.join(cont):
                            # print('全部：', cont)
                            inf = GetHTTPS.rawToDic(raw)  # 格式转化
                            if type(inf) == dict:
                                try:
                                    for v in inf.keys():
                                        inf[v] = unquote(inf[v])  # 对raw字典的url字符进行格式转化
                                        # print(inf)
                                        return inf
                                        # GetHTTPS.li.append(inf)
                                    # print(li)
                                except:
                                    # GetHTTPS.li.append("null")
                                    return None
                            else:
                                return inf
                        elif 'multipart/form-data' in ''.join(cont):
                            inf = GetHTTPS.rawToDic(raw)  # 格式转化

                            if type(inf) == dict:
                                try:
                                    for v in inf.keys():
                                        inf[v] = unquote(inf[v])  # 对raw字典的url字符进行格式转化
                                        # print(inf)
                                        return inf
                                        # GetHTTPS.li.append(inf)
                                    # print(li)
                                except:
                                    # GetHTTPS.li.append("null")
                                    return None
                            else:
                                return inf
                        else:
                            print('非json/x-www/x-form', cont)
                            return None

                else:
                    # print("非post")
                    return None
                    # GetRespon.reli.append('null')

    #返回一个raw字典
    def rawToDic(raw):
        # print('raw:', raw)
        try:
            vals = raw.split('&')
            for val in vals:
                dic = dict(val.split('=') for val in raw.split('&'))
                for key in dic:
                    GetHTTPS.inftab.append(str(key))
                    print('x-www-tab', GetHTTPS.inftab)
                return dic
        except:
            return raw


        '''    
        if raw and raw.startswith('{'):  # 如果是字典格式，直接写到list里
            globals = {
                'true': 0,
                'null': 0,
                'false': 0
            }
            ra = eval(raw, globals)
            for key in ra.keys():
                # print("tab:", key)
                GetHTTPS.inftab.append(key)
                # print("直接添加tab")
            # print(ra)
            return ra
        elif raw and '&' in raw:  # x-www格式
            # print(type(raw), raw)
            # print("进行格式转化")
            print("raw:", raw)
            # print("type:", type(d), d)
            # di = eval(str)
            try:
                d = dict(x.split("=") for x in raw.split("&"))  # 分割str字符串
                for key in d.keys():
                    # print("正常格式")
                    GetHTTPS.inftab.append(key)
            except:
                # print("非正常格式")
                d = {}
                GetHTTPS.li.append("null")
            # print("d:", type(d), d)
            return d
        elif raw:

            # print("非post")
            GetRespon.reli.append('null')'''

    def wList(path, rlis, name):
        ftxt = path + name
        fp = open(ftxt, 'a', errors='ignore')
        for rli in rlis:
            fp.write(str(rli) + '\n')
        fp.close()

    #修改保存地址
    def wSum(stri):
        path = 'I:/IoTSensitiveDataAnalysis/数据/设备抓包/三星.txt'
        with open(path, 'a', errors='ignore') as f:
            f.writelines(str(stri)+'\n')
            f.close()

    def wrTab(path, rlis, name):
        ftxt = path + name
        fp = open(ftxt, 'w', errors='ignore')
        for rli in rlis:
            fp.write(str(rli) + '\n')
        fp.close()

if __name__ == "__main__":
    path = "I:/IoTSensitiveDataAnalysis/数据/设备抓包/orisaz/三星sum/raw/"
    GetHTTPS.getTxt(path)

    # print(GetHTTPS.inftab)
    # GetHTTPS.wList(path, GetHTTPS.inftab, "phlips_A_连接_ctab.txt")  #把c的标签导出到txt
    # GetHTTPS.wList(path, GetRespon.reinftab, "phlips_A_连接_stab.txt") #把服务器返回的信息里的标签导出到txt

    #tabs = []
    #for i in GetHTTPS.inftab + GetRespon.reinftab:
        #if not i in tabs:
            #tabs.append(i)
    #print("所有tab:", tabs)
    savepath = "I:/IoTSensitiveDataAnalysis/数据/设备抓包/"
    GetHTTPS.wrTab(savepath, set(GetHTTPS.inftab), "SamsungSum.txt")
    #print("所有信息：", GetHTTPS.li + GetRespon.reli)
    # lis = GetHTTPS.li + GetRespon.reli
    # GetHTTPS.wList(savepath, lis, "oppo_手环__allinfo.txt")
    # print(len(GetHTTPS.li))
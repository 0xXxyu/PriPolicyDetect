# coding=utf-8
import http.client
import hashlib
import urllib
import random
import json

class BingTrans:

    def tran(st):

        url = '/v2/Http.svc/Translate'
        fromLang = 'en'  # 原文语种
        toLang = 'zh'  # 译文语种
        appId = 'A4D660A48A6A97CCA791C34935E4C02BBB1BEC1C'
        myurl = url + '?appId='+appId +'&from=' + fromLang + '&to=' + toLang +'&text='+ urllib.parse.quote(
            st)

        print("url:", myurl)
        try:
            httpClient = http.client.HTTPConnection('api.microsofttranslator.com')
            httpClient.request('GET', myurl)

            # response是HTTPResponse对象
            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")

            lin = result_all.split('<', 2)[1]
            li = lin.split('>')[1]

            # print(li)
            return li

        except Exception as e:
            print(e)
            return st
        finally:
            if httpClient:
                httpClient.close()
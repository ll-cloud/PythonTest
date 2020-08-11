# coding=utf-8
import requests, json,jsonpath
from suds.client import Client
import json
import traceback
# from common import Encrypt

class SOAP:
    def __init__(self, w):
        # 请求的client
        self.client=None
        # 头的管理
        self.headers={}
        #
        self.wsdl=''
        # 返回值
        self.result = None
        self.jsonres = None
        # 关联保存的地址
        self.relations = {}
        # 写入ecxcel文件的Excel.Writer对象
        self.writer = w
        # 记录当前需要写入的行
        self.row = 0

    def setwsdl(self, url):
        """
        设置基本wsdl地址
        :param url:
        :return:
        """
        self.wsdl=url
        self.client = Client(url)
        self.__write_excel_res('PASS', '设置成功：' + url)

    def __get_data(self, params):
        """
        处理字符串'username=1&password=2'
        :param params:
        :return:
        """
        if params is None or params == '':
            return None
        else:
            return params.split('、')

    def callmethod(self, name, params):
        """
        发送callmethod请求
        :param name:
        :param params:
        :return:
        """
        params = self.__get_relations(params)
        # params=self.__user_encrypt(params)
        params=self.__get_data(params)
        try:
            if params is None:
                self.result=self.client.service.__getattr__(name)()
            else:
                self.result=self.client.service.__getattr__(name)(*params)
        except:
            self.result=str(traceback.format_exc())

        try:
            self.jsonres = json.loads(self.result)
        except:
            self.jsonres == None
        self.__write_excel_res('PASS', self.result)


        # self.jsonres = json.loads(self.result.text)
        # try:
        #     self.jsonres = json.loads(self.result)
        # except:
        #     self.jsonres == None
        # self.__write_excel_res('PASS', self.result)

        print(self.jsonres)

    def logout(self, path):
        """
        发送logout请求
        :param path:
        :return:
        """
        self.result = self.session.post(self.url + path)

    def addheader(self, key, value):
        """
        添加头域
        :param key: 键
        :param value: 值
        :return:
        """
        value = self.__get_relations(value)
        self.headers[key] = value
        self.client=Client(self.wsdl,headers=self.headers)
        self.__write_excel_res('PASS', '添加成功' + str(self.headers))

    def removeheader(self, key):
        """
        删除头域里面的某一个键值对
        :param key: 要删除的键
        :return:
        """
        try:
            self.headers.pop(key)
        except:
            pass
        self.client=Client(self.wsdl)
        self.__write_excel_res('PASS', '删除成功' + str(self.headers))

    def savejson(self, key, param_name):
        """
        保存关联的参数
        :param key:需要保存的json结果里面的键
        :param param_name:保存后的名字
        :return:
        """
        try:
            self.relations[param_name] = self.jsonres[key]
            self.__write_excel_res('PASS', 'msg:' + str(self.relations))
        except Exception as e:
            self.relations[param_name] = ''
            self.__write_excel_res('FAIL', 'msg：' + str(self.relations))

    def __get_relations(self, params):
        """
        将参数里面用到关联的地方，替换成关联后的值
        :param params: 关联前的参数
        :return: 关联后的结果
        """
        if params is None or params == '':
            return ''
        else:
            for key in self.relations:
                params = params.replace('{' + key + '}', self.relations[key])
        return params

    # def assertequals(self, key, value):
    #     """
    #     判断json结果里面某个键的值是否与期望值value相等
    #     :param key: json的键
    #     :param value: 期望值
    #     :return: 是否相等
    #     """
    #     res = None
    #     try:
    #         res = str(self.jsonres[key])
    #     except Exception as e:
    #         pass
    #     print(value)
    #     print(self.__get_relations(value))
    #     value = self.__get_relations(value)
    #     if res == value:
    #         self.__write_excel_res('PASS', 'msg:' + str(res))
    #         return True
    #     else:
    #         self.__write_excel_res('FAIL', 'msg:' + str(res))
    #         return False

    def assertequals(self, jsonpathkey, value):
        """
        判断json结果里面某个键的值是否与期望值value相等
        :param key: json的键
        :param value: 期望值
        :return: 是否相等
        """
        res = None
        try:
            res = str(jsonpath.jsonpath(self.jsonres,jsonpathkey)[0])
        except Exception as e:
            pass
        print(value)
        print(self.__get_relations(value))
        value = self.__get_relations(value)
        if res == value:
            self.__write_excel_res('PASS', 'msg:' + str(res))
            return True
        else:
            self.__write_excel_res('FAIL', 'msg:' + str(res))
            return False

    def __write_excel_res(self, status, msg):
        # 写入excel
        self.writer.write(self.row, 7, status)
        self.writer.write(self.row, 8, str(msg))

    # def __user_encrypt(self,params):
    #     if params is None:
    #         return ''
    #     elif params.find('[')>=0 & params.find(']')>0:
    #         en_s=params[params.find('[')+1:params.find(']')]
    #         en_s1=Encrypt.encrpy(en_s)
    #         params = params.replacr('['+en_s+']',en_s1)
    #         return  self.user_encrypt(params)
    #     else:
    #         return  params

# coding=utf-8
import requests, json


class HTTP:
    def __init__(self):
        # session管理
        self.session = requests.session()
        # 基础的host地址
        self.url = ''
        # 返回值
        self.result = None
        self.jsonres = None

    def seturl(self, url):
        """
        设置基本url地址
        :param url:
        :return:
        """
        self.url = url

    def __getdata__(self,params):
        """
        处理字符串'username=1&password=2'
        :param params:
        :return:
        """
        if params is None or params=='':
            return None
        else:
            params_dict={}
            list_params=params.split('&')
            for param in list_params:
                # key_values=params.split('=')
                if param.find('=') >= 0:
                    params_dict[param[0:param.find('=')]] = param[param.find('=') + 1:]
                else:
                    params_dict[param] = None
            return params_dict
    def post(self, path, params):
        """
        发送post请求
        :param path:
        :param params:
        :return:
        """
        self.result = self.session.post(self.url + path, data=self.__getdata__(params))
        self.jsonres = json.loads(self.result.text)
        print(self.jsonres)

    def addheader(self, key, value):
        """
        添加头域
        :param key: 键
        :param value: 值
        :return:
        """
        self.session.headers[key] = value

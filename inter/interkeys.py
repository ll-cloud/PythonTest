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
        # 关联保存的地址
        self.relations={}

    def seturl(self, url):
        """
        设置基本url地址
        :param url:
        :return:
        """
        self.url = url

    def __getdata(self,params):
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
        params = self.__get_relations(params)
        self.result = self.session.post(self.url + path, data=self.__getdata(params))
        self.jsonres = json.loads(self.result.text)
        print(self.jsonres)

    def addheader(self, key, value):
        """
        添加头域
        :param key: 键
        :param value: 值
        :return:
        """
        value=self.__get_relations(value)
        self.session.headers[key] = value

    def savejson(self,key,param_name):
        """
        保存关联的参数
        :param key:需要保存的json结果里面的键
        :param param_name:保存后的名字
        :return:
        """
        self.relations[param_name]=self.jsonres[key]

    def __get_relations(self,params):
        """
        将参数里面用到关联的地方，替换成关联后的值
        :param params: 关联前的参数
        :return: 关联后的结果
        """
        if params is None or params=='':
            return ''
        else:
            for key in self.relations:
                params=params.replace('{'+key+'}',self.relations[key])
        return params

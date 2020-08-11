from appium import webdriver
import time
import traceback
import os,threading

from common import logger

class App:
    """
    封装app自动化的常用操作
    """

    def __init__(self, w):
        # 定义实例变量，存储浏览器，这个浏览器可以在整个类中使用‘
        self.driver = None
        self.txt = None
        # 写入结果
        self.row = 0
        self.writer = w
        # 关联的参数
        self.relations = {}
        # app启动的参数字典
        self.conf={}

    def __write_excel_res(self, status, msg):
        # 写入excel
        self.writer.write(self.row, 7, status)
        self.writer.write(self.row, 8, str(msg))

    def appconf(self,conf):
        """
        配置操作app:appium客户端配置的json字符串
        :param conf:
        :return:
        """
        try:
            conf=conf.replace('\n','')
            self.conf=eval(conf)
            self.__write_excel_res('PASS', '配置成功')
            os.popen('adb connect %s' % self.conf['deviceName'])
        except Exception as e:
            logger.error('配置格式错误')
            logger.exception(e)
            self.__write_excel_res('FAIL', '配置格式错误'+str(traceback.format_exc()))

    def startappium(self, apppath):
        def run(cmd):
            os.popen(cmd).read()

        # 创建一个线程
        cmd = 'node '+apppath+'\\Appium\\resources\\app\\node_modules\\appium\\build\\lib\\main.js'
        res = os.popen('netstat -aon |findstr 4723').read().split()
        if len(res)>0 and len(res[0]) > 1:
            self.__write_excel_res('FAIL', '端口被占用' + str(res))
        else:
            th = threading.Thread(target=run, args=(cmd,))
            th.start()
            time.sleep(6)
            self.__write_excel_res('PASS', 'appium正在运行')

    def stopappium(self, apppath):
        os.popen('taskkill /F /IM node.exe')

    def linkappium(self):
        """
        连接appium
        :return:
        """
        try:
            driver = webdriver.Remote("http://localhost:4723/wd/hub", self.conf)
            self.driver = driver
            self.driver.implicitly_wait(10)
            self.__write_excel_res('PASS', '连接appium成功')
        except Exception as e:
            self.__write_excel_res('FAIL', traceback.format_exc())
            exit(-1)

    def clear(self,xpath):
        ele = self.__find_by_xpath(xpath)
        ele.clear()
        self.__write_excel_res('PASS', '文本清空成功')

    def click_by_xpath(self, xpath):
        """
        点击元素
        :param xpath:定位元素的xpath
        :return:
        """
        ele = self.__find_by_xpath(xpath)
        ele.click()
        self.__write_excel_res('PASS', '点击元素成功')

    def input_by_xpath(self, xpath, value):
        """
        输入文本
        :param xpath:定位元素的xpath
        :param value:需要输入的文本内容
        :return:
        """
        ele = self.__find_by_xpath(xpath)
        ele.send_keys(value)
        self.__write_excel_res('PASS', '写入文本成功')

    def get_text_by_xpath(self, xpath, paramname):
        """
        获取元素的文本
        :param xpath:
        :return:
        """
        try:
            ele = self.__find_by_xpath(xpath)
            self.relations[paramname] = ele.text
            self.__write_excel_res('PASS', '获取元素文本' + self.relations[paramname] )
            return self.relations[paramname]
        except:
            self.relations[paramname] = ''
            self.__write_excel_res('FAIL', traceback.format_exc())

    def __find_by_xpath(self, xpath):
        """
        封装xpath的方法
        :param xpath:定位元素的xpath
        :return:找到的元素，如果没找到，返回none
        """
        if xpath.__contains__(':id/')>0:
            ele = self.driver.find_element_by_id(xpath)
        elif xpath.startswith('/'):
            ele = self.driver.find_element_by_xpath(xpath)
        else:
            ele = self.driver.find_element_by_accessibility_id(xpath)
        return ele

    def sleep(self, t=1):
        """
        显示等待
        :param t: 时间
        :return:
        """
        if t is None or t == '':
            t = 1
        else:
            t = int(t)

        time.sleep(t)
        self.__write_excel_res('PASS', 'sleep成功')

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

    def assert_equal(self, paramname, expect_value):
        """
        校验文本是否与期望值一样
        :param paramname: 参数
        :param expect_value: 期望值
        :return:
        """
        paramname = self.__get_relations(paramname)
        if (not paramname is None) and paramname == expect_value:
            print("校验成功")
            self.__write_excel_res('PASS', '断言成功：' + expect_value)
            return True
        else:
            print("校验失败")
            self.__write_excel_res('FAIL', '断言失败')
            return False

    def quit(self):
        self.driver.quit()
        self.__write_excel_res('PASS', '退出成功')

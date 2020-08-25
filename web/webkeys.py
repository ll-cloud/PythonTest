from selenium import webdriver
import time
import traceback

from selenium.webdriver import ActionChains

from common import logger

class Web:
    """
    封装web自动化的常用操作
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

    def __write_excel_res(self, status, msg):
        # 写入excel
        self.writer.write(self.row, 7, status)
        self.writer.write(self.row, 8, str(msg))

    def openBrower(self, br=None, dr=None):
        """

        :param br: 指定打开的浏览器类型
                  （gc:谷歌浏览器，ff:火狐浏览器，ie:ie浏览器,默认gc）
        :param dr: 指定driver文件的位置,默认gcdriver路径
        :return:
        """
        if br is None or br == ' ':
            br = 'gc'
        try:
            if br == 'gc':
                dr = './web/lib/chromedriver'
                self.driver = webdriver.Chrome(executable_path=dr)
                # 隐式等待
                self.driver.implicitly_wait(10)
            elif br == "ff":
                dr = './web/lib/geckodriver'
                self.driver = webdriver.Firefox(executable_path=dr)
            elif br == "ie":
                dr = './web/lib/IEDriverServer'
                self.driver = webdriver.Ie(executable_path=dr)
            else:
                self.driver = webdriver.Chrome(executable_path=dr)
                # 隐式等待
                self.driver.implicitly_wait(10)
            self.__write_excel_res('PASS', '打开浏览器成功')
        except Exception as e:
            logger.exception(e)
            self.__write_excel_res('FAIL', traceback.format_exc())
            self.writer.save_close()
            # 程序在这个异常时候停止运行
            exit(-1)

    def geturl(self, url):
        """
        打开网站地址
        :param url: 网站地址，必须以http/https开头
        :return:
        """
        try:
            self.driver.get(url)
            self.__write_excel_res('PASS', '打开url成功')
        except Exception as e:
            self.__write_excel_res('FAIL', traceback.format_exc())

    def click_by_xpath(self, xpath):
        """
        点击元素
        :param xpath:定位元素的xpath
        :return:
        """
        ele = self.__find_by_xpath(xpath)
        ele.click()
        self.__write_excel_res('PASS', '点击元素成功')

    def click_link_by_xpath(self, xpath):
        """
        点击a标签，selenium点击不了的情况
        :param xpath:定位元素的xpath
        :return:
        """
        ele = self.__find_by_xpath(xpath)
        href = ele.get_attribute('href')
        self.geturl(href)
        self.__write_excel_res('PASS', '点击链接成功')

    def click_js_by_xpath(self, xpath):
        """
        点击a标签，selenium点击不了的情况
        (点击标签，触发js，适合javascript:void(0))
        :param xpath: 定位元素的xpath
        :return:
        """
        ele = self.__find_by_xpath(xpath)
        self.driver.execute_script('$(arguments[0]).click()', ele)
        self.__write_excel_res('PASS', '点击js成功')

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

    def get_title_by_xpath(self, paramname):
        """
        获取元素的文本
        :param paramname:
        :return:
        """
        try:
            self.relations[paramname] = self.driver.title
            self.__write_excel_res('PASS', '获取元素文本' + self.relations[paramname])
            return self.relations[paramname]
        except:
            self.relations[paramname] = ''
            self.__write_excel_res('FAIL', traceback.format_exc())

    def switch_window(self,idx):
        try:
            # 窗口下边的列表
            handles = self.driver.window_handles
            # 切换到制定下标的窗口
            self.driver.switch_to.window(handles[int(idx)])
            self.__write_excel_res('PASS', '切换窗口成功' + str(idx))
        except:
            self.__write_excel_res('FAIL', traceback.format_exc())

    def switch_iframe(self,xpath):
        try:
            ele=self.__find_by_xpath(xpath)
            self.driver.switch_to.frame(ele)
            self.__write_excel_res('PASS', 'ifram切换成功')
        except:
            self.__write_excel_res('FAIL', traceback.format_exc())

    def switch_out(self):
        try:
            # 切换到HTML页面，最外层
            self.driver.switch_to.default_content()
            self.__write_excel_res('PASS', 'ifram切换最外层成功')
        except:
            self.__write_excel_res('FAIL', traceback.format_exc())

    def move_to(self,xpath):
        """
        悬停操作
        :param xpath:
        :return:
        """
        try:
            ele=self.__find_by_xpath(xpath)
            # 把鼠标移动到元素
            actions=ActionChains(self.driver)
            actions.move_to_element(ele).perform() # perform是前面的操作生效

            self.__write_excel_res('PASS', '悬停操作成功')
        except:
            self.__write_excel_res('FAIL', traceback.format_exc())

    def excute_js(self,js):
        """
        悬停操作
        :param xpath:
        :return:
        """
        try:
            self.driver.execute_script(js)
            self.__write_excel_res('PASS', '执行js成功')
        except:
            self.__write_excel_res('FAIL', traceback.format_exc())


    def __find_by_xpath(self, xpath):
        """
        封装xpath的方法
        :param xpath:定位元素的xpath
        :return:找到的元素，如果没找到，返回none
        """
        ele = self.driver.find_element_by_xpath(xpath)
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

    def getverify(self,locator=''):
        """
        获取图文验证码
        :param locator: 验证码图片的定位器
        :return:
        """
        try:
            ele=self.__find_by_xpath(locator)
            # 截取验证码图片
            ele.screenshot('./lib/images/verify.png')
            self.__write_excel_res('PASS', '截图成功')
        except:
            self.__write_excel_res('FAIL', traceback.format_exc())

    def quit(self):
        self.driver.quit()
        self.__write_excel_res('PASS', '退出成功')

from selenium import webdriver
import time


class WebKeys:
    """
    封装web自动化的常用操作
    """

    def __init__(self):
        # 定义实例变量，存储浏览器，这个浏览器可以在整个类中使用‘
        self.driver = None
        self.txt = None

    def openBrower(self, br=None, dr=None):
        """

        :param br: 指定打开的浏览器类型
                  （gc:谷歌浏览器，ff:火狐浏览器，ie:ie浏览器,默认gc）
        :param dr: 指定driver文件的位置,默认gcdriver路径
        :return:
        """
        if (br is None or br == ' '):
            br = 'gc'
        if br == 'gc':
            dr='./lib/chromedriver'
            self.driver = webdriver.Chrome(executable_path=dr)
            # 隐式等待
            self.driver.implicitly_wait(10)
        elif br == "ff":
            dr = './lib/geckodriver'
            self.driver = webdriver.Firefox(executable_path=dr)
        elif br == "ie":
            dr = './lib/IEDriverServer'
            self.driver = webdriver.Ie(executable_path=dr)
        else:
            self.driver = webdriver.Chrome(executable_path=dr)
            # 隐式等待
            self.driver.implicitly_wait(10)


    def geturl(self, url):
        """
        打开网站地址
        :param url: 网站地址，必须以http/https开头
        :return:
        """
        self.driver.get(url)

    def click_by_xpath(self, xpath):
        """
        点击元素
        :param xpath:定位元素的xpath
        :return:
        """
        ele = self.__find_by_xpath(xpath)
        ele.click()

    def click_link_by_xpath(self, xpath):
        """
        点击a标签，selenium点击不了的情况
        :param xpath:定位元素的xpath
        :return:
        """
        ele = self.__find_by_xpath(xpath)
        href=ele.get_attribute('href')
        self.geturl(href)

    def click_js_by_xpath(self, xpath):
        """
        点击a标签，selenium点击不了的情况
        (点击标签，触发js，适合javascript:void(0))
        :param xpath: 定位元素的xpath
        :return:
        """
        ele = self.__find_by_xpath(xpath)
        self.driver.execute_script('$(arguments[0]).click()',ele)


    def input_by_xpath(self, xpath, value):
        """
        输入文本
        :param xpath:定位元素的xpath
        :param value:需要输入的文本内容
        :return:
        """
        ele = self.__find_by_xpath(xpath)
        ele.send_keys(value)

    def get_text_by_xpath(self, xpath):
        """
        获取元素的文本
        :param xpath:
        :return:
        """
        ele = self.__find_by_xpath(xpath)
        self.txt = ele.text
        return self.txt

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

    def assert_equal(self, expect_value):
        """
        校验文本是否与期望值一样
        :param expect_value: 期望值
        :return:
        """
        if self.txt == expect_value:
            print("校验成功")
            return True
        else:
            print("校验失败")
            return False

    def quit(self):
        self.driver.quit()

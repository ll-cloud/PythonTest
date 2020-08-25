# coding=utf-8
from common import config
from common.Excel import Reader, Writer
from inter.interkeys import HTTP
from inter.soapkeys import SOAP
from web.webkeys import Web
import inspect
from common.mysql import Mysql
from app.appkeys import App

print("我的数据驱动测试框架 ")


def runcase(line, obj):
    """
    执行每一行用例
    :param line: 用例的数据列表
    :param obj: 执行用例的关键字对象
    :return: 无
    """
    # obj=HTTP()
    # 反射获取要执行的关键字
    func = getattr(obj, line[3])
    # 执行要获取的参数列表
    parmas = inspect.getfullargspec(func).__str__()

    parmas = parmas[parmas.find('args=') + 5:parmas.find(', varargs')]
    parmas = eval(parmas)
    parmas.remove('self')
    # 执行
    if len(parmas) == 0:
        func()
        return
    elif len(parmas) == 1:
        func(line[4])
        return
    elif len(parmas) == 2:
        func(line[4], line[5])
        return
    elif len(parmas) == 3:
        func(line[4], line[5], line[6])
        return
    else:
        print('暂时不支持超过3个参数的关键字')


# 读取配置信息
config.get_config('./conf/conf.properties')
# 数据库初始化
mysql = Mysql()
mysql.init_mysql('./conf/userinfo.sql')
# 逐行读取excel
casename = 'Web'
reader = Reader()
reader.open_excel('./lib/cases/%s.xls' % casename)
writer = Writer()
writer.copy_open('./lib/cases/%s.xls' % casename, './lib/results/result-%s.xls' % casename)

sheetname = reader.get_sheets()
reader.readline()
casetype = reader.readline()[1]
obj = None  # 执行用例的关键字对象
if casetype == 'HTTP':
    # 执行http接口自动化
    obj = HTTP(writer)
elif casetype == 'SOAP':
    obj = SOAP(writer)
elif casetype == 'WEB':
    obj = Web(writer)
elif casetype == 'APP':
    obj = App(writer)
for sheet in sheetname:
    # 设置当前读取的sheet页面
    reader.set_sheet(sheet)
    # 读到哪个sheet页写到哪里
    writer.set_sheet(sheet)
    for i in range(reader.rows):
        line = reader.readline()
        # 读到哪一行写哪一行
        obj.row = i
        if len(line[0]) > 0 or len(line[1]) > 0:
            # 分组信息，不用执行
            pass
        else:
            print(line)
            # 执行用例
            runcase(line, obj)
writer.save_close()

# print('我的第一个测试框架')
# 读取配置文件信息
# config.get_config('./conf/conf.properties')
# print(config.config)

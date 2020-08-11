import os,jpype
# 需要导入的jar位置
jarpath='./lib/encrypt.jar'
# 获取java路径
jdkpath=os.environ['JAVA_HOME']

# 启动jvm,加载jar
jpype.startJVM(jdkpath+'/jre/bin/server/jvm.dll','-ea','-Djava.calss.path=%s'%jarpath,
               convertStrings=False)

# 获取jar中的类
JClass=jpype.JClass('com.testing.will.Encrypt')
# 初始化类，就是执行构造函数
instance=JClass('.\lib\cwetificate.jks')


def encrypt(s):
    """"""

    # 调用加密函数，instance相当于java对象
    result=str(instance.enCrypt(s))
    return result


def decrypt(s):
    #调用解密函数
    result=str(instance.deCrypt(s))
    return result


def shutdown():

    # 关闭jvm
    jpype.shutdownJVM()
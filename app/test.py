import os,threading

# 多线程
def run(cmd):
    res=os.popen(cmd).read()
    print(res)

# 创建一个线程
cmd= 'node C:\\Users\\大圣\\AppData\\Local\\Programs\\Appium\\resources\\app\\node_modules\\appium\\build\\lib\\main.js'
res=os.popen('netstat -aon |findstr 4723').read().split()

th=threading.Thread(target=run,args=(cmd,))
th.start()
print(111)
# 结束
th.join()

from inter.interkeys import HTTP
import inspect

http=HTTP('w')
# 从http这个实例对象里面获取到post这个属性或者方法
# func等价于http.post
func=getattr(http,'post')
# 获取参数列表
s=inspect.getfullargspec(func).__str__()
print(s)
s=s[s.find('args=')+5:s.find(', varargs')]
s=eval(s)
s.remove('self')
print(s)
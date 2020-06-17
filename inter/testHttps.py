from inter.interkeys import HTTP

# 创建一个请求库的实例对象
http = HTTP()

http.seturl('http://www.testingedu.com.cn:8081/inter/HTTP/')
http.post('auth', None)
http.savejson('token','token')
# 添加token进头域
http.addheader('token', '{token}')
# 2. 登录

# params = {
#     'username': 'ly02',
#     'password': '123456'
# }
# http.post('login', params)
http.post('login', 'username=ly02&password=123456')
# 保存userId
http.savejson('userid','userId')
# 3.查询用户信息
# http.post('getUserInfo', {'id': http.jsonres['userid']})
http.post('getUserInfo', 'id={userId}')
# 4.退出

http.post('logout', None)

from suds.client import Client
import json

# 创建请求webservices的客户端
client = Client('http://www.testingedu.com.cn:8081/inter/SOAP?wsdl') # wsdl文档的位置4
# 使用客户端调服务器的接口
# res=client.service.auth()
res = client.service.__getattr__('auth')()
# print(res)
headers={
    'token':json.loads(res)['token']
}

client = Client('http://www.testingedu.com.cn:8081/inter/SOAP?wsdl',headers=headers) # wsdl文档的位置4

params=['Will','123456']
res=client.service.login(*params)  # 500没传参
print(res)
res=client.service.logout()
print(res)
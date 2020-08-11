import requests,json,jsonpath

session=requests.session()
session.headers['referer']='https://ke.qq.com/course/317690'
res=session.get('https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=317690&count=10&page=0&filter_rating=1&bkn=&r=0.44521002852860714')
print(res.text)
jsonres=json.loads(res.text)
value=jsonpath.jsonpath(jsonres,'$.result.total_num')
print(value[0])
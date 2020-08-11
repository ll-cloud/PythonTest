from class07.web import Web

webobj = Web()

# 打开浏览器
webobj.openBrower("gc")

# 访问网站
webobj.geturl('http://www.testingedu.com.cn:8000/index.php')
# 点击登录按钮
webobj.click_by_xpath('//a[text()="登录"]')
# 填写登录信息
webobj.input_by_xpath('//input[@placeholder="手机号/邮箱"]', '70536024@qq.com')
webobj.input_by_xpath('//input[@placeholder="密码"]', '123456')
webobj.input_by_xpath('//input[@placeholder="验证码"]', '12345')
# 点击登录按钮
webobj.click_by_xpath('//a[@class="J-login-submit"]')

# 校验

webobj.get_text_by_xpath('//a[@class="home"]')
webobj.assert_equal("返回商城首页")

# 退出浏览器
webobj.quit()



# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/4 16:05
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：allure测试报告生成
"""
import pytest
import allure
import os


@pytest.fixture(scope='function')
def login():
    print("登录")
    yield
    print("登录完成")


def test_cart(login):
    """将手机加入购物车"""
    print("添加购物车1")


def test_cart1():
    """将电脑加入购物车"""
    print("添加购物车2")


if __name__ == "__main__":
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    # pytest.main(['--alluredir', './temp']) # 执行所有的测试报表
    pytest.main(['./test_allure.py','--alluredir', './temp'])  # 执行某一个的测试报表
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system('allure generate ./temp -o ./report --clean')

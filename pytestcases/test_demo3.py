import pytest

class Test_ABC:
    # def setup_class(self):
    #     print("----SetUp class")
    #
    # def setup(self):
    #     print("----SetUp")
    #
    # def teardown_class(self):
    #     print('\n----teardown_class')

    @pytest.fixture()
    def a_set_up_teardown(self):
        print('开始a')
        yield
        print('结束a')

    def test_a(self,a_set_up_teardown):
        print('----test_a')
        assert True

    def test_b(self):
        print('----test_b')
        assert False


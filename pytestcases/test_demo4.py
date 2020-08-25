# -*- coding: UTF-8 -*-
from pytestcases.my_mo import add
import pytest

class Test_Add:
    @pytest.mark.parametrize("x,y,z,name", [
        [1, 1, 2,'整数加整数'],
        [1, 1.01, 2.01,'整数加小数'],
        # [1, '1', 'error','整数加字符串']
    ])
    def test_add(self, x, y, z,name):
        assert add(x, y) == z

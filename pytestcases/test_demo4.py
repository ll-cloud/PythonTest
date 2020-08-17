from my_mo import add
import pytest

class Test_Add:

    @pytest.mark.parametrize("x,y,z",[
        [1,1,2],
        [1,1.01,2.01],
        [1,'1','error']
    ])
    def test_add(self, x, y, z):
        assert add(x, y) == z

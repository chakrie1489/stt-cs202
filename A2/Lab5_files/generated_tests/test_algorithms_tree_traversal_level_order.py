# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import algorithms.tree.traversal.level_order as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 2559
    module_0.level_order(int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
    var_0 = module_0.level_order(set_0)
    bool_0 = True
    module_0.level_order(bool_0)

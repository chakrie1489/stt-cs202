# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import algorithms.tree.traversal.zigzag as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    module_0.zigzag_level(bool_0)


def test_case_1():
    set_0 = set()
    var_0 = module_0.zigzag_level(set_0)

# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import algorithms.arrays.missing_ranges as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    tuple_0 = ()
    set_0 = {tuple_0, tuple_0, tuple_0}
    module_0.missing_ranges(set_0, tuple_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    var_0 = module_0.missing_ranges(tuple_0, tuple_0, tuple_0)
    set_0 = {tuple_0, tuple_0, tuple_0}
    module_0.missing_ranges(set_0, tuple_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -1858
    module_0.missing_ranges(int_0, int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -1569
    list_0 = [int_0, int_0]
    bytes_0 = b"\xa1\xef\x10!\x97\xc2"
    module_0.missing_ranges(list_0, bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    tuple_0 = ()
    var_0 = module_0.missing_ranges(tuple_0, tuple_0, tuple_0)
    str_0 = "t[e#*5;9%jy"
    module_0.missing_ranges(var_0, tuple_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "RDKwH[FGV^^E:\x0c2ot"
    module_0.missing_ranges(str_0, str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    tuple_0 = ()
    float_0 = -2416.742
    float_1 = -2795.0872
    var_0 = module_0.missing_ranges(tuple_0, float_0, float_1)
    bool_0 = False
    module_0.missing_ranges(var_0, bool_0, tuple_0)

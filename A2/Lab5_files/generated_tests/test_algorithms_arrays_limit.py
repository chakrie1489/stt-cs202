# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import algorithms.arrays.limit as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    tuple_0 = ()
    var_0 = module_0.limit(tuple_0, tuple_0)
    var_1 = module_0.limit(var_0)
    bool_0 = True
    var_2 = module_0.limit(tuple_0, max_lim=var_0)
    str_0 = "c\\mNJ"
    tuple_1 = (bool_0, str_0)
    none_type_0 = None
    module_0.limit(tuple_1, max_lim=none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    int_0 = -2912
    set_0 = set()
    tuple_0 = (bool_0, int_0, set_0)
    module_0.limit(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 1166
    dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0}
    var_0 = module_0.limit(dict_0)
    module_0.limit(dict_0, max_lim=var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "hI"
    var_0 = module_0.limit(str_0)
    var_1 = module_0.limit(str_0, max_lim=str_0)
    var_2 = module_0.limit(str_0)
    var_3 = module_0.limit(var_2, str_0)
    module_0.limit(var_2, var_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    none_type_0 = None
    module_0.limit(none_type_0)

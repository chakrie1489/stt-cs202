# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import algorithms.arrays.longest_non_repeat as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = -1990.36889
    none_type_0 = None
    var_0 = module_0.longest_non_repeat_v2(none_type_0)
    assert var_0 == 0
    var_1 = module_0.longest_non_repeat_v2(none_type_0)
    assert var_1 == 0
    var_2 = module_0.longest_non_repeat_v1(none_type_0)
    assert var_2 == 0
    module_0.get_longest_non_repeat_v3(float_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -3822.14
    module_0.longest_non_repeat_v1(float_0)


def test_case_2():
    none_type_0 = None
    var_0 = module_0.longest_non_repeat_v2(none_type_0)
    assert var_0 == 0
    bytes_0 = b"\xd4\x95\x0cZ4n\x9c,\x7f'\xb9\xd9\x0b"
    var_1 = module_0.get_longest_non_repeat_v1(bytes_0)


def test_case_3():
    bytes_0 = b"D\xa3\xcc?\xa6\xcc_\xa2\xb3\xb2\xa7\xaf\xd7\xa5dq"
    var_0 = module_0.longest_non_repeat_v2(bytes_0)
    assert var_0 == 13


def test_case_4():
    none_type_0 = None
    var_0 = module_0.get_longest_non_repeat_v1(none_type_0)
    bytes_0 = b"\x81\x11\xb3\x9b\xc5\x8b\xfd@\x15\n\xb6\xa8\xf4\xa1\x93\x16\xc2\xd6\xca"
    var_1 = module_0.get_longest_non_repeat_v1(bytes_0)
    var_2 = module_0.get_longest_non_repeat_v1(var_1)


@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = 4736
    module_0.get_longest_non_repeat_v1(int_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "Yu ;D!:o+\tF\\DC"
    var_0 = module_0.get_longest_non_repeat_v1(str_0)
    none_type_0 = None
    var_1 = module_0.get_longest_non_repeat_v2(none_type_0)
    set_0 = {var_0}
    var_2 = module_0.longest_non_repeat_v2(set_0)
    assert var_2 == 1
    module_0.get_longest_non_repeat_v3(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    bool_0 = False
    module_0.get_longest_non_repeat_v2(bool_0)


def test_case_8():
    tuple_0 = ()
    bytes_0 = b"\xf1\xe7\xb6\xea\x05\x7f\xe5"
    tuple_1 = (tuple_0, bytes_0)
    var_0 = module_0.get_longest_non_repeat_v3(tuple_1)
    var_1 = module_0.longest_non_repeat_v1(var_0)
    assert var_1 == 2


@pytest.mark.xfail(strict=True)
def test_case_9():
    set_0 = set()
    var_0 = module_0.get_longest_non_repeat_v1(set_0)
    list_0 = [var_0, set_0, set_0]
    module_0.longest_non_repeat_v1(list_0)


@pytest.mark.xfail(strict=True)
def test_case_10():
    bytes_0 = b"v\xc2\xf9$\x1c\xb8\x8a*\xc0+\xd9)\xf9"
    var_0 = module_0.get_longest_non_repeat_v2(bytes_0)
    var_1 = module_0.longest_non_repeat_v2(bytes_0)
    assert var_1 == 12
    module_0.get_longest_non_repeat_v1(var_1)


@pytest.mark.xfail(strict=True)
def test_case_11():
    bytes_0 = b"[[@l\xfcxy[1,\xf4\x94\x0cs\x8b\xf70"
    var_0 = module_0.get_longest_non_repeat_v1(bytes_0)
    var_1 = module_0.get_longest_non_repeat_v3(var_0)
    var_2 = module_0.longest_non_repeat_v2(var_1)
    assert var_2 == 2
    var_3 = module_0.get_longest_non_repeat_v3(bytes_0)
    module_0.get_longest_non_repeat_v2(var_2)


@pytest.mark.xfail(strict=True)
def test_case_12():
    bytes_0 = b"\xe4FFu\xa1\xf2)\xd9V\xec\x02"
    var_0 = module_0.longest_non_repeat_v1(bytes_0)
    assert var_0 == 9
    bytes_1 = b"\xc5\xab\xb6\xaf\x8eMn\xfd"
    var_1 = module_0.get_longest_non_repeat_v2(bytes_1)
    var_2 = module_0.longest_non_repeat_v2(bytes_0)
    assert var_2 == 9
    module_0.get_longest_non_repeat_v3(var_2)


@pytest.mark.xfail(strict=True)
def test_case_13():
    str_0 = "Yu ;D!:o+\tF\\DC"
    var_0 = module_0.get_longest_non_repeat_v1(str_0)
    none_type_0 = None
    set_0 = {var_0}
    var_1 = module_0.longest_non_repeat_v2(set_0)
    assert var_1 == 1
    module_0.get_longest_non_repeat_v3(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_14():
    str_0 = "=~#-%5]c}~<aZ["
    var_0 = module_0.get_longest_non_repeat_v3(str_0)
    float_0 = -176.254
    module_0.longest_non_repeat_v1(float_0)


@pytest.mark.xfail(strict=True)
def test_case_15():
    str_0 = "\nGiven a sorted integer array without duplicates,\nreturn the summary of its ranges.\n\nFor example, given [0, 1, 2, 4, 5, 7], return [(0, 2), (4, 5), (7, 7)].\n"
    var_0 = module_0.get_longest_non_repeat_v3(str_0)
    var_1 = module_0.longest_non_repeat_v2(str_0)
    assert var_1 == 14
    module_0.get_longest_non_repeat_v1(var_1)


def test_case_16():
    bytes_0 = b"\x83A\x8c\x8bO\xc0+.\xed\x9b\x16\x96\x81YQ\x8f\t"
    var_0 = module_0.get_longest_non_repeat_v2(bytes_0)
    var_1 = module_0.get_longest_non_repeat_v2(var_0)
    var_2 = module_0.get_longest_non_repeat_v1(var_1)
    var_3 = module_0.get_longest_non_repeat_v3(bytes_0)
    var_4 = module_0.longest_non_repeat_v1(var_0)
    assert var_4 == 2
    none_type_0 = None
    var_5 = module_0.get_longest_non_repeat_v1(var_0)
    var_6 = module_0.longest_non_repeat_v2(var_0)
    assert var_6 == 2
    var_7 = module_0.get_longest_non_repeat_v1(none_type_0)
    var_8 = module_0.longest_non_repeat_v2(var_3)
    assert var_8 == 2
    str_0 = "E<q4#*:!xx]`I)wLQPs"
    var_9 = module_0.get_longest_non_repeat_v2(str_0)


def test_case_17():
    str_0 = "t0 HdXB03"
    var_0 = module_0.get_longest_non_repeat_v1(str_0)
    var_1 = module_0.get_longest_non_repeat_v2(var_0)
    var_2 = module_0.longest_non_repeat_v2(var_1)
    assert var_2 == 2
    tuple_0 = ()
    var_3 = module_0.get_longest_non_repeat_v2(tuple_0)
    bytes_0 = b"\x83A\x8c\x8bO\xc0+.\xed\x9b\x16\x96\x81YQ\x8f\t"
    var_4 = module_0.get_longest_non_repeat_v2(bytes_0)
    var_5 = module_0.get_longest_non_repeat_v3(var_0)
    var_6 = module_0.get_longest_non_repeat_v2(var_4)
    var_7 = module_0.get_longest_non_repeat_v2(var_1)
    var_8 = module_0.get_longest_non_repeat_v1(str_0)
    var_9 = module_0.get_longest_non_repeat_v3(bytes_0)
    var_10 = module_0.longest_non_repeat_v1(var_4)
    assert var_10 == 2
    var_11 = module_0.get_longest_non_repeat_v2(var_0)
    none_type_0 = None
    var_12 = module_0.get_longest_non_repeat_v1(var_4)
    bool_0 = True
    tuple_1 = (var_6, var_1, var_5, bool_0)
    var_13 = module_0.longest_non_repeat_v2(var_5)
    assert var_13 == 2
    var_14 = module_0.get_longest_non_repeat_v2(var_12)
    var_15 = module_0.get_longest_non_repeat_v2(var_5)
    var_16 = module_0.get_longest_non_repeat_v3(tuple_1)
    var_17 = module_0.longest_non_repeat_v2(none_type_0)
    assert var_17 == 0
    var_18 = module_0.get_longest_non_repeat_v1(var_8)
    var_19 = module_0.longest_non_repeat_v1(var_11)
    assert var_19 == 2
    var_20 = module_0.longest_non_repeat_v1(bytes_0)
    assert var_20 == 17
    str_1 = 'sI}DiLqr`Q{A"L5;A{v'
    var_21 = module_0.longest_non_repeat_v2(var_18)
    assert var_21 == 2
    var_22 = module_0.get_longest_non_repeat_v2(str_1)

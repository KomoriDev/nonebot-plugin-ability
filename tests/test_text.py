def test_indent():
    from nonebot_plugin_ability.text import indent

    text = """
    Row 1
    Row 2
    Row 3
    """
    result = "Row 1\nRow 2\nRow 3"
    assert indent(text) == result


def test_md5():
    from nonebot_plugin_ability.text import md5

    text = "Hello World"
    result = "b10a8db164e0754105b7a99be72e3fe5"
    assert md5(text) == result

    text = "你好，世界"
    result = "dbefd3ada018615b35588a01e216ae6e"
    assert md5(text) == result


def test_random_string():
    from nonebot_plugin_ability.text import random_string

    result = random_string(8)
    assert len(result) == 8
    assert result.isalpha()

    result = random_string(6, type="numeric")
    assert len(result) == 6
    assert result.isdigit()

    result = random_string(5, prefix="ABC", type="alpha")
    assert len(result) == 5
    assert result.isalpha()
    assert result.startswith("ABC")

    result = random_string(6, type="alphanumeric", num_strings=3)
    assert len(result) == 3
    assert all(len(s) == 6 for s in result)
    assert all(s.isalnum() for s in result)

    result = random_string(10, charset="ABCD1234")
    assert len(result) == 10
    assert all(c in "ABCD1234" for c in result)

    result1 = random_string(10, seed=123)
    result2 = random_string(10, seed=123)
    assert result1 == result2

    result = random_string(8, start_index=2, end_index=5)
    assert len(result) == 4
    assert result.isalpha()

    result = random_string(6, prefix="ABC", start_index=1, end_index=4)
    assert len(result) == 4
    assert result.isalpha()
    assert result.startswith("ABC")

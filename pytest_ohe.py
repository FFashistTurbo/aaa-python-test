import pytest
from one_hot_encoder import fit_transform


def test_ft():
    first_case_input = ['Moscow', 'New York', 'Moscow', 'London']
    expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
    ]
    actual = fit_transform(first_case_input)

    assert actual == expected
    assert ('Moscow', [1, 0, 1]) not in expected


def test_nums():
    second_case_input = [1, 2, 3]
    expected = [
            (1, [0, 0, 1]),
            (2, [0, 1, 0]),
            (3, [1, 0, 0]),
    ]
    actual = fit_transform(second_case_input)

    assert actual == expected
    assert (1, [1, 0, 1]) not in expected


def test_empty_value():
    assert fit_transform("") == [('', [1])]


def test_raises_error():
    with pytest.raises(TypeError):
        fit_transform(42)

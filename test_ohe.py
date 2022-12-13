import unittest
from one_hot_encoder import fit_transform


class TestOhe(unittest.TestCase):
    def test_ft(self):
        first_case_input = ['Moscow', 'New York', 'Moscow', 'London']
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        actual = fit_transform(first_case_input)

        self.assertEqual(actual, expected)
        self.assertNotIn(('Moscow', [1, 0, 1]), expected)

    def test_nums(self):
        second_case_input = [1, 2, 3]
        expected = [
            (1, [0, 0, 1]),
            (2, [0, 1, 0]),
            (3, [1, 0, 0]),
        ]
        actual = fit_transform(second_case_input)

        self.assertEqual(actual, expected)
        self.assertNotIn((1, [1, 0, 1]), expected)

    def test_empty_value(self):
        self.assertEqual(fit_transform(""), [('', [1])])

    def test_raises_error(self):
        with self.assertRaises(TypeError):
            fit_transform(42)


if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import MagicMock, patch

from what_is_year_now import what_is_year_now


class TestYearNow(unittest.TestCase):
    def get_mock(self, resp):
        mock_tmp = MagicMock()
        mock_tmp.read.return_value = resp
        mock_tmp.__enter__.return_value = mock_tmp
        return mock_tmp

    @patch('urllib.request.urlopen')
    def test_first_format(self, mock_urlopen):
        resp = '{"currentDateTime": "2022-12-12T21:12Z", "utcOffset": "00:00:00"}'
        mock_urlopen.return_value = self.get_mock(resp)
        self.assertEqual(what_is_year_now(), 2022)

    @patch('urllib.request.urlopen')
    def test_second_format(self, mock_urlopen):
        resp = '{"currentDateTime": "12.12.2022", "utcOffset": "00:00:00"}'
        mock_urlopen.return_value = self.get_mock(resp)
        self.assertEqual(what_is_year_now(), 2022)

    @patch('urllib.request.urlopen')
    def test_wrong_data_format(self, mock_urlopen):
        resp = '{"currentDateTime": "01_03_2022"}'
        mock_urlopen.return_value = self.get_mock(resp)
        with self.assertRaises(ValueError):
            what_is_year_now()

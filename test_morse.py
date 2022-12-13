import pytest
from morse import decode


@pytest.mark.parametrize(
    "source_string,result",
    [
        ("-- .- ..", "MAI"),
        ("... --- ...", "SOS"),
        ("", "")
    ],
)
def test_decode(source_string, result):
    assert decode(source_string) == result

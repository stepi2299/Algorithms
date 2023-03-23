from n import find as find0
from kmp import find as find1
from kr import find as find2
import pytest


@pytest.mark.parametrize("find", [find0, find1, find2])
def test_empty_pattern(find):
    pattern = ""
    text="ABCDA"
    out_list = find(pattern, text)
    assert out_list == []


@pytest.mark.parametrize("find", [find0, find1, find2])
def test_empty_text(find):
    pattern = "ABCDA"
    text = ""
    out_list = find(pattern, text)
    assert out_list == []


@pytest.mark.parametrize("find", [find0, find1, find2])
def test_pattern_equal_text(find):
    pattern = "ABCDA"
    text = "ABCDA"
    out_list = find(pattern, text)
    assert out_list == [0]


@pytest.mark.parametrize("find", [find0, find1, find2])
def test_find_one_pattern(find):
    pattern = "ABCDA"
    text = "YUOABCDA"
    out_list = find(pattern, text)
    assert len(out_list) == 1
    assert pattern == text[out_list[0]:out_list[0]+len(pattern)]


@pytest.mark.parametrize("find", [find0, find1, find2])
def test_find_several_one_pattern(find):
    pattern = "ABCDA"
    text = "ABCDAYUOABCDAasdasABCDApopABCDAllllljbuokjnABsCsDfA"
    out_list = find(pattern, text)
    assert len(out_list) == 4
    for idx in out_list:
        assert pattern == text[idx:idx+len(pattern)]


@pytest.mark.parametrize("find", [find0, find1, find2])
def test_pattern_longer_than_text(find):
    pattern = "ABCDAA"
    text = "ABCDA"
    out_list = find(pattern, text)
    assert out_list == []


@pytest.mark.parametrize("find", [find0, find1, find2])
def test_pattern_not_in_text(find):
    pattern = "acd"
    text = "ABCDAacDACD"
    out_list = find(pattern, text)
    assert out_list == []


@pytest.mark.parametrize("find", [find0, find1, find2])
def test_empty_text_and_pattern(find):
    out_list = find("", "")
    assert out_list == []


@pytest.mark.parametrize("find", [find0, find1, find2])
def test_find_pattern_with_polish_letters(find):
    pattern = "źĄć"
    text = "śRuÓbżźĄfźĄćgŃ"
    out_list = find(pattern, text)
    assert len(out_list) == 1
    assert pattern == text[out_list[0]:out_list[0]+len(pattern)]


@pytest.mark.parametrize("find", [find0, find1, find2])
def test_crossing_pattern_in_text(find):
    pattern = "cc"
    text = "abcccba"
    out_list = find(pattern, text)
    assert len(out_list) == 2


@pytest.mark.parametrize("find", [find0, find1, find2])
def test_multiple_crossing_pattern_in_text(find):
    pattern = "aaaaa"
    text = "abaaaaaaabab"
    out_list = find(pattern, text)
    assert len(out_list) == 3

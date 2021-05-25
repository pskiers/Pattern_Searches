from algorithms import find_N, find_KMP, find_KR
import random


def test_empty_string():
    string = ''
    text = 'abcdehudus'
    assert find_N(string, text) == find_KMP(string, text) == find_KR(string, text) == []


def test_empty_text():
    text = ''
    string = 'adsew'
    assert find_N(string, text) == find_KMP(string, text) == find_KR(string, text) == []


def test_empty_text_and_string():
    text = ''
    string = ''
    assert find_N(string, text) == find_KMP(string, text) == find_KR(string, text) == []


def test_string_longer_than_text():
    text = 'abcdef'
    string = 'abcdefas'
    assert find_N(string, text) == find_KMP(string, text) == find_KR(string, text) == []


def test_string_same_as_text():
    text = 'abcdef'
    string = 'abcdef'
    assert find_N(string, text) == find_KMP(string, text) == find_KR(string, text) == [0]


def test_string_not_in_text():
    text = 'wheyyqjgefhywg'
    string = 'abc'
    assert find_N(string, text) == find_KMP(string, text) == find_KR(string, text) == []


def test_naive():
    text = 'abcdefabcdefabc'
    string = 'abc'
    assert find_N(string, text) == [0, 6, 12]
    text = 'Ala ma kota, a kot ma Alę'
    string = 'kot'
    assert find_N(string, text) == [7, 15]
    text = 'swswowswssswsw'
    string = 'sw'
    assert find_N(string, text) == [0, 2, 6, 10, 12]
    text = 'abcdefabababcbabcdefababcbababcababcbab'
    string = 'ababcbab'
    assert find_N(string, text) == [8, 20, 31]


def test_all_random():
    text = str([random.choice(['a', 'b']) for _ in range(1200)])
    strings = []
    string = str([random.choice(['a', 'b']) for _ in range(6)])
    strings.append(string)
    string = str([random.choice(['a', 'b']) for _ in range(2)])
    strings.append(string)
    string = str([random.choice(['a', 'b']) for _ in range(1)])
    strings.append(string)
    string = str([random.choice(['a', 'b']) for _ in range(150)])
    strings.append(string)
    string = str([random.choice(['a', 'b']) for _ in range(4)])
    strings.append(string)
    for word in strings:
        assert find_N(word, text) == find_KMP(word, text) == find_KR(word, text)

from typing import List


def find_N(string: str, text: str) -> List[int]:
    """
    Parameters:
    string (str): szukany napis
    text (str): przeszukiwany tekst
    Returns:
    (list): lista pozycji w 'text' (w kolejności rosnącej), od których zaczyna się 'string'
    """
    if len(string) == 0 or len(text) == 0 or len(string) > len(text):
        return []
    results = []
    for pos in range(len(text)-len(string)+1):
        correct = True
        for letpos in range(len(string)):
            if string[letpos] != text[pos + letpos]:
                correct = False
                break
        if correct:
            results.append(pos)
    return results


def find_KMP(string: str, text: str) -> List[int]:
    """
    Parameters:
    string (str): szukany napis
    text (str): przeszukiwany tekst
    Returns:
    (list): lista pozycji w 'text' (w kolejności rosnącej), od których zaczyna się 'string'
    """
    if len(string) == 0 or len(text) == 0 or len(string) > len(text):
        return []

    def prefix_fuc(string: str) -> List[int]:
        lenght = len(string)
        result = [0 for _ in range(lenght)]
        k = 0
        for q in range(1, lenght):
            while k > 0 and string[k] != string[q]:
                k = result[k]
            if string[k] == string[q]:
                k += 1
            result[q] = k
        return result

    result = list()
    n = len(text)
    m = len(string)
    pi = prefix_fuc(string)
    q = 0
    for i in range(n):
        while (q > 0 and string[q] != text[i]):
            q = pi[q-1]
        if string[q] == text[i]:
            q = q + 1
        if q == m:
            result.append(i-m+1)
            q = pi[q-1]
    return result


def find_KR(string: str, text: str) -> List[int]:
    """
    Parameters:
    string (str): szukany napis
    text (str): przeszukiwany tekst
    Returns:
    (list): lista pozycji w 'text' (w kolejności rosnącej), od których zaczyna się 'string'
    """
    if len(string) == 0 or len(text) == 0 or len(string) > len(text):
        return []
    result = []
    string = [ord(x) for x in string]
    text = [ord(x) for x in text]
    d = 512
    q = 393241
    m = len(string)
    n = len(text)
    h = (d ** (m-1)) % q
    p = 0
    t = 0
    for i in range(m):
        p = (d*p + string[i]) % q
        t = (d*t + text[i]) % q
    for s in range(n-m+1):
        if p == t:
            if string == text[s:s+m]:
                result.append(s)
        if s < n-m:
            t = (d*(t-text[s]*h) + text[s+m]) % q
    return result

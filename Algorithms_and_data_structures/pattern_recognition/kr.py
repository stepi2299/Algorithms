""" Alfabet wykorzystywany do testów jednostkowych """
import string
alphabet = string.ascii_letters
alphabet += "ĄąĆćĘęŁłŃńÓóŚśŹźŻż0123456789"

""" Alfabet wykorzystywany do Pana Tadeusza """
# alphabet = 'Adam Mickewz\nPnTusylotjLISBN978-3245KęgprGó—,łWżśąŻOźbRE!:ć.DJCh(f;ń)ZŚUFé?…«H»ÓŁxv*àŹV/Ćq1æ–06'

import time

letter_value = {}
cnt = 0
for letter in alphabet:
    letter_value[letter] = cnt
    cnt += 1

# modulo operator
Q = 997


def find(template: str, text: str) -> list:
    indexes = []
    m = len(text)
    n = len(template)
    k = len(alphabet)
    if n == 0 or n > m: return indexes
    temp_hash = hash_string(template, Q)
    text_hash = hash_string(text[0:n], Q)

    if temp_hash == text_hash and check(template, text, 0):
        indexes.append(0)

    for i in range(1, m-n+1):
        text_hash = (text_hash + Q - letter_value[text[i-1]] * k ** (n-1) % Q)
        text_hash = (text_hash * k + letter_value[text[i+n-1]]) % Q
        if temp_hash == text_hash and check(template, text, i):
            indexes.append(i)

    return indexes


def hash_string(text, Q):
    m = len(text)
    n = len(alphabet)
    hash_value = 0
    for i in range(1, m + 1):
        hash_value += letter_value[text[-i]] * n ** (i - 1)
    return hash_value % Q


def check(template, text, pos):
    m = len(text)
    n = len(template)
    if n + pos > m: return False
    for i in range(n):
        if text[pos + i] != template[i]:
            return False
    return True

""" Alfabet wykorzystywany do testów jednostkowych """
import string
alphabet = string.ascii_letters
alphabet += "ĄąĆćĘęŁłŃńÓóŚśŹźŻż0123456789"

""" Alfabet wykorzystywany do Pana Tadeusza """
# alphabet = 'Adam Mickewz\nPnTusylotjLISBN978-3245KęgprGó—,łWżśąŻOźbRE!:ć.DJCh(f;ń)ZŚUFé?…«H»ÓŁxv*àŹV/Ćq1æ–06'

def find(template: str, text: str) -> list:
    n = len(text)
    m = len(template)
    template_idxes = []
    i = j = 0
    dfa = _dfa_creation(template)
    while i < n and j < m:
        j = dfa[text[i]][j]
        i += 1
        if j == m:
            template_idxes.append(i-m)
            i += 1 - m
            j = 0

    return template_idxes


def _dfa_creation(template):
    m = len(template)
    dfa = {}
    if m>0:
        for ch in alphabet:
            dfa[ch] = [0]*m
        x = 0
        j = 1
        dfa[template[0]][0] = 1
        while j < m:
            for c in template:
                dfa[c][j] = dfa[c][x]
            dfa[template[j]][j] = j+1
            x = dfa[template[j]][x]
            j += 1
    return dfa

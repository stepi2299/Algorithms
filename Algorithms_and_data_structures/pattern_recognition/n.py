def find(template: str, text: str) -> list:
    indexes = []
    m = len(text)
    n = len(template)
    if n == 0: return indexes
    pattern_found = True
    for i in range(0, m):
        pattern_found = True
        for j in range(0, n):
            if i + j >= m or text[i+j] != template[j]:
                pattern_found = False
                break
        if pattern_found: indexes.append(i)
    return indexes

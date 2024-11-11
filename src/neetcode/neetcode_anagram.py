
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    idx_map = {}
    for i in range(len(s)):
        # they have to have same words each
        # so if we pick a word from s, then t should have same word at different place
        picked = s[i]
        prev = idx_map.get(picked, -1)
        idx = t.find(picked, prev + 1)
        if idx == -1:
            return False
        idx_map[picked] = idx

    return True

if __name__ == '__main__':
    print(isAnagram('racecar', 'carrace'))
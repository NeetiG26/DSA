''' Isomorphic Strings'''

def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    elif len(s)==len(t)==1:
        return True
    else:
        map_s = {}
        # map_t = {}
        is_isomorphic = True
        for i in range(len(s)):
            if s[i] not in map_s.keys():
                map_s[s[i]] = t[i]
            if s[:i+1].count(s[i]) != t[:i+1].count(map_s[s[i]]):
                
                is_isomorphic = False
                
        return is_isomorphic
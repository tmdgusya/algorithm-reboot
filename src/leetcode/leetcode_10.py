class Solution(object):

    def separate_pattern(self, p):
        prev = ""
        groups = []
        tmp = []
        ANY = "."
        ALL = "*"
        def is_concatable(c1, c2):
            if (c1 != ANY and c1 != ALL) and (c2 == ANY or c2 == ALL):
                return True
            return False 
        
        for i, c in enumerate(p):
            if i == 0 and len(p) > 1:
                tmp.append(c)
                prev = c
                continue
            
            if prev == c:
                tmp.append(c)
            elif is_concatable(prev, c):
                groups.append(
                    {
                        "patterns": tmp + [c],
                        "isMacthed": False
                    }
                )
                tmp = []
            else: 
                if len(tmp) == 0:
                    tmp.append(c)
                    groups.append({
                        "patterns": tmp,
                        "isMatched": False
                    })
                else:
                    groups.append({
                        "patterns": tmp,
                        "isMatched": False
                    })

                    groups.append({
                        "patterns": [c],
                        "isMatched": False
                    })

                tmp = []
            prev = c
        
        return groups

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        POINTER = 0

        """
        - aaaaaaaab
        - .*b
        - a*b
        """

        """
        1. separate s into group of same word
        2. separate p into group of same word or union
        3. check each groups can be matched
        """
        print(self.separate_pattern(p))

            
        return "f"
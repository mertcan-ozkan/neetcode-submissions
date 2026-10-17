class Solution:
    from typing import List

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
    
        for word in strs:
            char_count = {}
    
            for letter in word:
                if letter in char_count:
                    char_count[letter] += 1
                else:
                    char_count[letter] = 1
    
            # dictionaries cannot be used as dictionary keys,
            # so convert it to a hashable representation
            key = tuple(sorted(char_count.items()))
    
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
    
        return list(groups.values())




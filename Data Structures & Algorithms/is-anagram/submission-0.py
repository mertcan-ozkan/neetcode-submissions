class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str_dict  = {}
        str_dict_2 = {}
        for letter in s:
            if letter not in str_dict:
                str_dict[letter] = 1
            else:
                str_dict[letter] = str_dict[letter] + 1
        for letter in t:
            if letter not in str_dict_2:
                str_dict_2[letter] = 1
            else:
                str_dict_2[letter] +=1     
        return  str_dict_2== str_dict
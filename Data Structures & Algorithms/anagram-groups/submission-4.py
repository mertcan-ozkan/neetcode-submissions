class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for input_string in strs:
            letter_dict: dict[str, int] = {}
            for letter in input_string:
                if letter in letter_dict:
                    letter_dict[letter] +=1
                else:
                    letter_dict[letter] = 1
            key = tuple(sorted(letter_dict.items()))
        
            if key not in groups:
                groups[key] = []

            groups[key].append(input_string)

        return list(groups.values())
            

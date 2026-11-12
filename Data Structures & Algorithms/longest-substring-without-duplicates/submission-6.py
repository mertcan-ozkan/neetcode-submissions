class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars:set[str,int] = set()
        max_lengths:list[int] = []
        longest = 0
        max_lengths.append(longest)
        start_idx = 0

        for i,char in enumerate(s):
            if char not in unique_chars:
                unique_chars.add(char)
                longest +=1
            else:
                while char in unique_chars:
                    unique_chars.remove(s[start_idx])
                    start_idx += 1
                unique_chars.add(char)
                max_lengths.append(longest)
                longest = len(unique_chars)

        if  len(unique_chars) != 0:
            max_lengths.append(len(unique_chars))

        return max(max_lengths)
            
            
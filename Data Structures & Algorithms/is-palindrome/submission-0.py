class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        i_start =0
        i_end = len(s)-1

        while(i_start<=i_end ):
            if(s[i_start]!=s[i_end]):
                return False
            i_start +=1
            i_end -=1
        return True

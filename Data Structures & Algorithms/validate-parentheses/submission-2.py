class Solution:
    def isValid(self, s: str) -> bool:
        stack_l = []
        left_paran = {'(':0,'{':1,'[':2}
        right_paran = {')':0,'}':1,']':2}
        for letter in s :
            if letter in left_paran:
                stack_l.append(letter)
            elif letter in right_paran:
                if len(stack_l)==0:
                    return False
                last_letter = stack_l.pop()
                if left_paran[last_letter] != right_paran[letter]:
                    return False
        if len(stack_l)!=0:
            return False
        return True
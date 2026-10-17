class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference_set = {}
        for index, num in enumerate(nums):
            difference = target - num
            if difference in difference_set:
                return [difference_set[difference], index]
            else:
                difference_set[num] = index

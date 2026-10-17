class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = {}

        for num in nums:
            if num in frequency_dict:
                frequency_dict[num] += 1
            else:
                frequency_dict[num] = 1

        reversed_d = {}

        for num, frequency in frequency_dict.items():
            if frequency not in reversed_d:
                reversed_d[frequency] = []

            reversed_d[frequency].append(num)

        keys = sorted(reversed_d, reverse=True)

        res = []

        for frequency in keys:
            for num in reversed_d[frequency]:
                res.append(num)

                if len(res) == k:
                    return res
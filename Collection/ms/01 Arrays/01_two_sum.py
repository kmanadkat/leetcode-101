class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dt = {}
        for index, num in enumerate(nums):

            # Check If Complement Exists in dictionary
            complement = target - num
            if complement in dt and dt[complement] != index:
                return [index, dt[complement]]

            # Add entry for future checks
            dt[num] = index

        return []

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elems = {}

        for i in range(len(nums)):
            if target - nums[i] in elems:
                return [elems[target - nums[i]], i]
            else:
                elems[nums[i]] = i
        return []
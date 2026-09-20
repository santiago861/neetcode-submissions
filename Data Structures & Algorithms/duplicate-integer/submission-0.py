class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elems = set()
        for i in nums:
            if i in elems:
                return True
            else:
                elems.add(i)
        return False
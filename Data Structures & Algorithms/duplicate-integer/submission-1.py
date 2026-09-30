class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myNums = set()
        for num in nums:
            if num in myNums:
                return True
            myNums.add(num)
        return False

        
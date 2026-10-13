class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        return sorted(count, key=lambda x: count[x], reverse=True)[0]
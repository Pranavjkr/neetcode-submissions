class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        hashSet = set()

        for r in range(len(nums)):
            if r - l > k:
                hashSet.remove(nums[l])
                l += 1
            
            if nums[r] in hashSet:
                return True
                
            hashSet.add(nums[r])
        
        return False

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap={}
        for i,num in enumerate(nums):
            if num in hashmap:
                if (i-hashmap.get(num))<=k:
                    return True
                else:
                    hashmap[num]=i
            else:
                hashmap[num]=i
        return False
#two sums
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

class Solution:
    def twoSum(self,nums:list [int],target:int)-> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] == target-nums[i]:
                    return [i,j]
        return[]
    

#now with hastables 

class Solution:
    def twoSum(self,nums:list[int],target;int) -> list[int]:
        hasmap = {}
        for i in range(len(nums)):
            hasmap[nums[i]]=i
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hasmap and hasmap[complement] !=i:
                return [i,hasmap[complement]]
            
        return[]

 
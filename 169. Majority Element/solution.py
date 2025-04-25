def majorityElement(nums: list[int]) -> int:
    res = majority = 0
    for n in nums:
        if majority == 0:
            res = n            
        majority += 1 if n == res else -1
    return res
print(majorityElement([2,2,1,1,1,2,2]))
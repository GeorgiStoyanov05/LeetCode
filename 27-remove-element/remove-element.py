def removeElement(nums: list[int], val: int) -> int:
        counter = 0
        index = 0
        while index<len(nums):
            if(nums[index]==val):
                  counter+=1
                  index-=1
                  nums.remove(val)
                  nums.append(0)
            index+=1
        return len(nums)-counter
print(removeElement([0,1,2,2,3,0,4,2], 2))
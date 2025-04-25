def rotate(nums: list[int], k: int) -> None:
    k = k%len(nums)
    n = len(nums) - k
    nums[:] = nums[n:] +nums[:n]
    return nums
rotate([1,2,3,4,5,6,7], 3)
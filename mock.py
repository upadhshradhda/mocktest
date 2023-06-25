def move_zeros_end(nums):
    i = 0
    for num in nums:
        if num != 0:
            
            nums[i] = num
            i += 1
    while i < len(nums):
        nums[i] = 0
        i += 1

    return nums
nums = [0,1,0,3,12]
result = move_zeros_end(nums)
print(result)

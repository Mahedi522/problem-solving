nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
i = 0
# for i in range(len(nums)):
while i < len(nums):
            
    def dele(i):
        print(i)
        if nums[i] == nums[i+1]:
            del nums[i+1]
            if i<len(nums):
                i = i+1
                dele(i)
    dele(i)
    i = i+1
print(len(nums))

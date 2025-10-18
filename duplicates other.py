nums = [1, 2, 3, 1]
print(len(nums) != len(set(nums)))


nums = [1, 2, 3, 1]
found = False
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            print("Duplicate found:", nums[i])
            found = True
print(found)

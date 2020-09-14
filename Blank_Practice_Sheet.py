def main():
    """
        Do not return anything, modify nums in-place instead.
        """
    nums = [7, 1, 2, 3, 4, 5, 6]
    k = 3
    print(nums)

    k = k % len(nums)
    i = 0
    while i < k:

        temp = nums.pop()
        print(temp)
        nums.insert(0, temp)
        i += 1

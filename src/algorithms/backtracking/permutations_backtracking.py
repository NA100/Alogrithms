def permutate(nums):
    res = []
    def backtrack(perm, nums, pick):
        if len(perm) == len(nums):
            res.append(perm[:])
            return

        for i in range(0, len(nums)):
            if not pick[i]:
                perm.append(nums[i])
                pick[i] = True
                backtrack(perm, nums, pick)
                perm.pop()
                pick[i]= False

    backtrack([], nums, [False] * len(nums))
    return res

if __name__ == "__main__":
    nums = [1, 2, 3]
    res = permutate(nums)
    print(res)
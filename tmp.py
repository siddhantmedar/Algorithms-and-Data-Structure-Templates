def test(nums):
    mp = {}
    sum = 0
    for i, ele in enumerate(nums):
        sum += ele
        if sum == 0:
            return True
        mp[sum] = i
    return False


if __name__ == "__main__":
    nums = [1, 2, 3, -7]
    print(test(nums))

def two_difference(arr, target):
    nums = {}

    for i, num in enumerate(arr):
        nums[num] = i

    for i in range(len(arr)):
        if target + arr[i] in nums:
            return [i, nums[target+arr[i]]]

    return [-1, -1]


def main():
    print(two_difference([6, 3, 2, 4, 12], 6))
    print(two_difference([6, 3, 4, 2], 3))


main()

def two_sum(nums, target):
    seen = {}

    for index, value in enumerate(nums):
        required = target - value

        if required in seen:
            return [seen[required], index]

        seen[value] = index

    return []

print(two_sum([2, 7, 11, 15], 9))
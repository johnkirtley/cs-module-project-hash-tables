nums = (1, 3, 4, 7, 12)

add_results = {}
sub_results = {}


def operations(x):
    return x * 4 + 6


def solve(nums):
    results = []

    for i in range(len(nums)):
        for j in range(len(nums)):
            add_results[(nums[i], nums[j])] = operations(
                nums[i]) + operations(nums[j])
            sub_results[(nums[i], nums[j])] = operations(
                nums[i]) - operations(nums[j])

    for i in add_results:
        for j in sub_results:
            if add_results[i] == sub_results[j]:
                result = f"{operations(i[0])} + {operations(i[1])} = {operations(j[0])} - {operations(j[1])}"
                results.append(result)

    return results


print(solve(nums))

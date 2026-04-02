def two_sum_sorted(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]  # 1-based index

        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []


# Example run
numbers = [2, 7, 11, 15]
target = 9
print(two_sum_sorted(numbers, target))
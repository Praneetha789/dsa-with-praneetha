# Two Pointer Technique

arr = [1, 2, 3, 4, 6]
target = 6

left = 0
right = len(arr) - 1

found = False

while left < right:

    current_sum = arr[left] + arr[right]

    if current_sum == target:
        print("Pair Found:",
              arr[left], arr[right])
        found = True
        break

    elif current_sum < target:
        left += 1

    else:
        right -= 1

if not found:
    print("No Pair Found")
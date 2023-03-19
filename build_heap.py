def build_heap(nums):
    swaps = []
    for i in range(len(nums)//2 - 1, -1, -1):
        left = 2 * i + 1
        right = 2 * i + 2
        current = i
        if left < len(nums) and nums[left] < nums[current]:
            current = left
        if right < len(nums) and nums[right] < nums[current]:
            current = right
        if current != i:
            swaps.append((i, current))
            swaps.append((i, current))
            nums[i], nums[current] = nums[current], nums[i]
    return swaps


def main():
    # Let's get some input from the user.
    text = input()

    if 'I' in text:
        n = int(input())
        data = list(map(int, input().split()))

    if 'F' in text:
        file_name = input()
        with open(file_name, 'r') as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))

    # Check that the data is valid.
    assert len(data) == n

    # Sort the data.
    swaps = build_heap(data)

    # Print the sorted data.
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

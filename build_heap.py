def build_heap(data, n):
    swaps = []

    for i in range(n // 2, -1, -1):
        num = i

        while True:
            left = 2 * i + 1
            if left < n and data[left] < data[num]:
                num = left
            right = 2 * i + 2

            if right < n and data[right] < data[number]:
                num = right

            if num != i:
                data[i], data[num] = data[num], data[i]
                swaps.append((i, num))
                i = num

            else:
                break

    return swaps


def main():
    imethod = input()

    if imethod.startswith("I"):
        n = int(input())
        data = list(map(int, input().split()))

    elif imethod.startswith("F"):
        file_name = input()
        file_path = "./tests/"

        if "a" not in file_name:
            with open(file_path + file_name, mode = "r") as file:
                n = int(file.readline())
                data = list(map(int, file.readline().split()))
        else:
            exit()
    else:
        exit()

    assert len(data) == n
    swaps = build_heap(data, n)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

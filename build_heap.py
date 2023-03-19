def build_heap(data, n):
    swaps = []

    for i in range(n // 2, -1, -1):
        num = i

        while True:
            left = 2 * i + 1
            if left < n and data[left] < data[num]:
                num = left
            right = 2 * i + 2

            if right < n and data[right] < data[num]:
                num = right

            if num != i:
                data[i], data[num] = data[num], data[i]
                swaps.append((i, num))
                i = num

            else:
                break

    return swaps


def main():
    imode = input().strip()

    if imode == "I":
        n = int(input())
        data = list(map(int, input().split()))

    elif mode == "F":
        filenam = input()
        with open("tests/" + filenam, 'r') as faili:
            n = int(faili.readline())
            data = list(map(int, faili.readline().split()))

    else:
        exit()

    assert len(data) == n
    swaps = build_heap(data, n)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

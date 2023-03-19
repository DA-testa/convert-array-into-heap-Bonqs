def build_heap(data, n):
    swaps = []
    
    for i in range(n // 2, -1, -1):
        number = i
        
        while True:
            left_branch = 2 * i + 1
            if left_branch < n and data[left_branch] < data[number]:
                number = left_branch
            right_branch = 2 * i + 2
            
            if right_branch < n and data[right_branch] < data[number]:
                number = right_branch
                
            if number != i:
                data[i], data[number] = data[number], data[i]
                swaps.append((i, number))
                i = number
                
            else:
                break

    return swaps


def main():
    input_method = input()
    
    if input_method.startswith("I"):
        n = int(input())
        data = list(map(int, input().split()))
        
    elif input_method.startswith("F"):
        print("File path: ")
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

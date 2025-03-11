from collections.abc import Sequence

def check_fibonacci(data: Sequence[int]) -> bool:
    #на минимальную длину
    if len(data) < 2:
        return len(data) == 0 or data[0] == 0 and (len(data) == 1 or data[1] == 1)

    for i in range(2, len(data)):
        if data[i] != data[i - 1] + data[i - 2]:
            return False
            
    return True

print(check_fibonacci([0, 1, 1, 2, 3, 5, 8]))  #true
print(check_fibonacci([0, 1, 1, 2, 4, 5]))   #false
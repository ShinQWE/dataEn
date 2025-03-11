from typing import List

def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    #инициализация макс суммы
    max_sum, current_sum = float('-inf'), 0
    for i in range(len(nums)):
        current_sum += nums[i]
         #вычитаем элемент
        if i >= k:
            current_sum -= nums[i - k]
        max_sum = max(max_sum, current_sum)
        #возвращаем макс сумму
    return max_sum if max_sum != float('-inf') else 0

nums = [1, 2, -1, -3, 5, 3, 6, 7]
k = 3
result = find_maximal_subarray_sum(nums, k)
print(result) #16
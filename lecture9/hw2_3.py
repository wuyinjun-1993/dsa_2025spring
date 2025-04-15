def shortestSubarray(nums, k):
    n = len(nums)
    min_len = float('inf')
    
    for i in range(n):
        current_max = nums[i]
        current_min = nums[i]
        for j in range(i, n):
            current_max = max(current_max, nums[j])
            current_min = min(current_min, nums[j])
            if current_max - current_min >= k:
                min_len = min(min_len, j - i + 1)
                break  # 找到满足条件的子数组后，可以提前终止内层循环
    
    return min_len if min_len != float('inf') else -1



import collections

def shortestSubarray(nums, k):
    n = len(nums)
    min_len = float('inf')
    min_deque = collections.deque()
    max_deque = collections.deque()
    left = 0

    for right in range(n):

        while min_deque and nums[right] < nums[min_deque[-1]]:
            min_deque.pop()
        min_deque.append(right)

        while max_deque and nums[right] > nums[max_deque[-1]]:
            max_deque.pop()
        max_deque.append(right)

        while left <= right and nums[max_deque[0]] - nums[min_deque[0]] >= k:
            min_len = min(min_len, right - left + 1)

            if min_deque[0] == left:
                min_deque.popleft()
            if max_deque[0] == left:
                max_deque.popleft()
            left += 1

    return min_len if min_len != float('inf') else -1


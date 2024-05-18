def num_subarrays_with_sum_at_least_k(arr, k):
    n = len(arr)
    start = 0
    current_sum = 0
    count = 0

    for end in range(n):
        current_sum += arr[end]
        while current_sum >= k:
            count += (n - end)
            current_sum -= arr[start]
            start += 1

    return count

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    k = 7
    print(num_subarrays_with_sum_at_least_k(arr, k))

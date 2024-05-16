def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def longest_palindrome(s):
    n = len(s)
    if n <= 1:
        return s

    dp = [[False] * n for _ in range(n)]
    start, max_len = 0, 1

    # 单个字符都是回文串
    for i in range(n):
        dp[i][i] = True
    # 遍历所有长度的子串
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2 or dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if length > max_len:
                        start = i
                        max_len = length

    return s[start:start + max_len]

# Example usage:
s = "babad"
print("Is palindrome:", is_palindrome(s))
print("Longest palindrome:", longest_palindrome(s))

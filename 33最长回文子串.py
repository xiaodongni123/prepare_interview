# @Date ：2024/07/18 21:28
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        count = 0

        for char in s:
            if char in char_set:
                char_set.remove(char)
                count += 2
            else:
                char_set.add(char)

        # 如果集合中还有字符，则可以在回文中心添加一个字符
        if char_set:
            count += 1

        return count


# 示例用法
solution = Solution()

# 示例 1
s1 = "abccccdd"
print(solution.longestPalindrome(s1))  # 输出: 7

# 示例 2
s2 = "a"
print(solution.longestPalindrome(s2))  # 输出: 1

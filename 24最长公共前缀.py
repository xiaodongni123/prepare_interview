# @Date ：2024/07/10 21:05
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # 取第一个字符串作为基准
        prefix = strs[0]

        for string in strs[1:]:
            # 更新公共前缀
            while string[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix


# 示例用法
solution = Solution()
strs1 = ["flower", "flow", "flight"]
print(solution.longestCommonPrefix(strs1))  # 输出: "fl"

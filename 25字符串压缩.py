# @Date ：2024/07/11 13:55
class Solution(object):
    def compressString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ""

        compressed = []
        count = 1

        for i in range(1, len(S)):
            if S[i] == S[i - 1]:
                count += 1
            else:
                compressed.append(S[i - 1] + str(count))
                count = 1

        # 添加最后一个字符及其计数
        compressed.append(S[-1] + str(count))

        compressed_str = ''.join(compressed)

        return compressed_str if len(compressed_str) < len(S) else S


# 示例用法
solution = Solution()
input1 = "aabcccccaaa"
print(solution.compressString(input1))  # 输出: "a2b1c5a3"

input2 = "abbccd"
print(solution.compressString(input2))  # 输出: "abbccd"

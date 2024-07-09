# @Date ：2024/07/09 19:44
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # 将版本号按照 '.' 分割成修订号列表
        v1_parts = version1.split('.')
        v2_parts = version2.split('.')

        # 获取最长的修订号列表长度
        max_length = max(len(v1_parts), len(v2_parts))

        # 逐个比较修订号
        for i in range(max_length):
            # 如果当前索引超过某个版本号的长度，则视为 0
            v1_part = int(v1_parts[i]) if i < len(v1_parts) else 0
            v2_part = int(v2_parts[i]) if i < len(v2_parts) else 0

            if v1_part < v2_part:
                return -1
            elif v1_part > v2_part:
                return 1

        # 如果所有修订号都相等，则返回 0
        return 0


# 示例用法
solution = Solution()
print(solution.compareVersion("1.2", "1.10"))  # 输出: -1
print(solution.compareVersion("1.01", "1.001"))  # 输出: 0
print(solution.compareVersion("1.0", "1.0.0"))  # 输出: 0
print(solution.compareVersion("0.1", "1.1"))  # 输出: -1

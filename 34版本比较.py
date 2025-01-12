# @Date ：2024/11/16 14:43
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        def parse_version(version):
            parts = []
            num = 0
            for char in version:
                if char == '.':
                    parts.append(num)
                    num = 0
                else:
                    num = num * 10 + int(char)
            parts.append(num)  # Append the last part
            return parts

        # Parse both versions manually
        v1_parts = parse_version(version1)
        v2_parts = parse_version(version2)

        # Compare parsed parts
        max_length = max(len(v1_parts), len(v2_parts))
        for i in range(max_length):
            v1 = v1_parts[i] if i < len(v1_parts) else 0
            v2 = v2_parts[i] if i < len(v2_parts) else 0

            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1

        return 0
solution = Solution()
print(solution.compareVersion("1.01", "1.001"))  # 输出: 0
print(solution.compareVersion("1.0", "1.0.0"))   # 输出: 0
print(solution.compareVersion("0.1", "1.1"))     # 输出: -1

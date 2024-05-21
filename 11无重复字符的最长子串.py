# @Date ：2024/05/20 20:37
"""
1. 双指针
2. 创建一个集合。存储出现过的
3. 如果字符不在集合中，将其添加到集合里，如果在集合中，移除到不重复为止
"""
def length_of_longest_substring(s):
    left = 0
    char_set = set()
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length


if __name__ == '__main__':
    s = "abcabcbb"
    print(length_of_longest_substring(s))
    #
    # s = "bbbbb"
    # print(length_of_longest_substring(s))

    s = "pwwkew"
    print(length_of_longest_substring(s))
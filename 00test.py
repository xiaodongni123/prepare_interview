def length_of_longest_substring(s):
    left = 0
    char_set  = set()
    max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right-left+1)
    return max_length


if __name__ == '__main__':
    # s = "abcabcbb"
    # print(length_of_longest_substring(s))

    # s = "bbbbb"
    # print(length_of_longest_substring(s))

    s = "pwwkew"
    print(length_of_longest_substring(s))
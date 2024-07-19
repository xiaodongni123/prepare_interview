# @Date ：2024/07/18 21:11
def bubblesort(s):
    for i in range(len(s)-1, -1, -1):
        for j in range(0, i):
            if s[j] > s[j + 1]:
                s[j + 1], s[j] = s[j], s[j + 1]


print(bubblesort([5, 2, 9, 1, 5, 6]))
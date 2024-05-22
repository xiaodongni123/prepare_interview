def isValid(s):
    # 1. 创建一个字典
    dic = {")" : "(", ']':'[', '}':'{'}
    # 2. 创建一个栈
    stack = []
    # 2. 遍历字典
    for i in s:
        # 3. if 栈不为空
        if stack and i in dic:
            # 能匹配上，弹出
            if stack[-1] == dic[i]:
                stack.pop()
            else:
                return False
        else:
            # 否则 return false
            stack.append(i)
    # 4. 返回栈的内容
    return not stack



if __name__ == '__main__':
    print(isValid("([)]"))
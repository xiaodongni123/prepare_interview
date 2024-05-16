# -*- coding:utf-8 -*-
# @Author ：xiaonijiang 
# @Date ：2024/05/15 15:41

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_end_point(head, n):
    dummy = ListNode()  # 创建虚拟头节点
    dummy.next = head

    fast = dummy
    slow = dummy
    count = 0

    while count < n:
        fast = fast.next
        count += 1

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = fast
    return dummy.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

n = 2

new_head = remove_end_point(head, n)

while new_head:
    print(new_head.val)
    new_head = new_head.next

"""
算法思想：
1. 定义一个链表类
2. 创建一个链表
3. 算法内容里面创建一个虚拟头节点
4. 定义快、慢指针
"""

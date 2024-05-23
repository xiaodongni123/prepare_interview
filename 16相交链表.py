# @Date ：2024/05/23 20:57

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getIntersectionNode( headA, headB):
    if headA is None or headB is None:
        return None
    pA, pB = headA, headB
    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA
    return pA


def build_list(nodes):
    head = ListNode(nodes[0])
    current = head
    for val in nodes[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

if __name__ == '__main__':
    # 示例1
    headA = build_list([4, 1, 8, 4, 5])
    headB = build_list([5, 6, 1])
    # 创建交点
    headB.next.next.next = headA.next.next
    print(getIntersectionNode(headA, headB).val)  # 输出: 8

    # 示例2
    headA = build_list([1, 9, 1, 2, 4])
    headB = build_list([3])
    # 创建交点
    headB.next = headA.next.next.next
    print(getIntersectionNode(headA, headB).val)  # 输出: 2

    # 示例3
    headA = build_list([2, 6, 4])
    headB = build_list([1, 5])
    print(getIntersectionNode(headA, headB))  # 输出: None



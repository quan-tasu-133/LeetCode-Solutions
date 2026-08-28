class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = curr = ListNode()
        carry = 0

        while l1 or l2:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next

            if l2:
                total += l2.val
                l2 = l2.next

            carry, digit = divmod(total, 10)
            curr.next = ListNode(digit)
            curr = curr.next

        if carry:
            curr.next = ListNode(carry)

        return dummy.next
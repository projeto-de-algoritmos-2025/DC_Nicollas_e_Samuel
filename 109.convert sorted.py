class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return None

        def convertToBST(start, end):
            if start == end:
                return None

            slow = start
            fast = start

            while fast != end and fast.next != end:
                slow = slow.next
                fast = fast.next.next

            root = TreeNode(slow.val)
            root.left = convertToBST(start, slow)
            root.right = convertToBST(slow.next, end)
            return root

        return convertToBST(head, None)
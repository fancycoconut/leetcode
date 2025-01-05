/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode DeleteDuplicates(ListNode head) {
        if (head is null) return null;

        var root = head;
        var prev = head;
        var current = head;
        while (current is not null)
        {
            // Remove current node if same as previous
            if (current.val == prev.val)
            {
                prev.next = current.next;
                current = current.next;
                continue;
            }

            prev = current;
            current = current.next;
        }

        return root;
    }
}
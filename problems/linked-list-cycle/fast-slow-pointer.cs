/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    // Using the fast slow pointer approach
    // aka Floyd's Cycle Finding Algorithm
    public bool HasCycle(ListNode head) {
        if (head is null) return false;

        var slow = head;
        var fast = head.next;
        while (slow != fast)
        {
            if (fast == null || fast.next == null) return false;

            slow = slow.next;
            fast = fast.next.next;
        }

        return true;
    }
}
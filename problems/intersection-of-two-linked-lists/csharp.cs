/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode GetIntersectionNode(ListNode headA, ListNode headB) {
        var nodes = new HashSet<ListNode>();
        var current = headA;
        while (current is not null)
        {
            nodes.Add(current);
            current = current.next;
        }

        current = headB;
        while (current is not null)
        {
            if (nodes.Contains(current)) return current;
            current = current.next;
        }

        return null;
    }
}
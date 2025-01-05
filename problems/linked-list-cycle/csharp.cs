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
    public bool HasCycle(ListNode head) {
        if (head is null || head.next is null) return false;

        var i = 0;
        var current = head;
        var map = new Dictionary<ListNode, int>();
        while (current is not null)
        {
            if (map.ContainsKey(current) && map[current] != i) return true;

            map[current] = i;
            i++;
            current = current.next;
        }

        return false;
    }
}
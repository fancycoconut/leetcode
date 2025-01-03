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

 // Naive bruteforce solution
public class Solution {
    public ListNode RemoveNthFromEnd(ListNode head, int n) {
        if (head.next is null) return null;

        // Get total number of nodes
        var total = 0;
        var end = head;
        while (end.next is not null)
        {
            end = end.next;
            total++;
        }

        total += 1;
        var nodeToRemoveIndex = total - n;
        if (n == total)
        {
            head = head.next;
            return head;
        }

        var current = head;
        var nodeBeforeNodeToRemove = head;
        for (var i = 0; i < total; i++)
        {
            if (i == nodeToRemoveIndex - 1)
            {
                Console.WriteLine($"Node before node to remove value: {current.val}");
                nodeBeforeNodeToRemove = current;
                break;
            }

            current = current.next;
        }

        var nodeToRemove = nodeBeforeNodeToRemove.next;
        var nextNodeAfterRemoval = nodeToRemove.next;
        nodeBeforeNodeToRemove.next = nextNodeAfterRemoval;

        return head;
    }
}
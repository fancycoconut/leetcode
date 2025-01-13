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
    // Using a stack as a solution
    public void ReorderList(ListNode head) {
        var length = 0;
        var current = head;
        var stack = new Stack<ListNode>();
        while (current is not null)
        {
            length++;
            stack.Push(current);
            current = current.next;
        }

        Console.WriteLine(length);

        current = head;
        for (var i = 0; i < length; i++)
        {
            var original = current;
            if (i % 2 == 0)
            {
                var n = stack.Pop();
                n.next = original.next;
                original.next = n;
            }
            current = current.next;
        }

        current.next = null;
    }
}
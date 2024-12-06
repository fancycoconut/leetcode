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
    public ListNode ReverseList(ListNode head) {
        if (head is null) return head;

        var current = head;
        var stack = new Stack<ListNode>();
        while (current.next is not null)
        {
            stack.Push(current);
            //Console.WriteLine($"Push - {current.val}");
            current = current.next;            
        }

        //Console.WriteLine($"Current: {current.val}");
        var root = current;
        while (stack.Count > 0)
        {
            var next = stack.Pop();
            //Console.WriteLine($"Pop - {next.val}");
            current.next = next;
            current = next;
        }

        current.next = null;

        return root;
    }
}
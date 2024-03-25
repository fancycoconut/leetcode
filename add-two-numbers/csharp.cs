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
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        var q1 = ConvertToStack(l1);
        var q2 = ConvertToStack(l2);

        var result = AddTogether(q1, q2);

        var node = ConvertToListNode(result);
        return node;
    }

    private ListNode ConvertToListNode(Queue<int> queue)
    {
        ListNode? node = null;
        while (queue.Any())
        {
            var val = queue.Dequeue();
            Console.WriteLine(val);
            
            if (node is null)
            {
                node = new ListNode(val);
            }
            else 
            {
                var newNode = new ListNode(val);
                node.next = newNode;
            }
        }

        return node;
    }

    private Queue<int> AddTogether(Queue<int> q1, Queue<int> q2)
    {
        var carry = 0;
        var queue = new Queue<int>();
        while (q1.Any() || q2.Any())
        {
            q1.TryDequeue(out var a);
            q2.TryDequeue(out var b);
            var sum = a + b + carry;
            //Console.WriteLine(sum);
            if (sum > 9)
            {
                carry = 1;
                sum = sum - 10;
            }
            else
            {
                carry = 0;
            }

            queue.Enqueue(sum);
        }

        if (carry != 0)
        {
            queue.Enqueue(carry);
        }

        return queue;
    }

    private static Queue<int> ConvertToStack(ListNode root)
    {
        var queue = new Queue<int>();

        var currentNode = root;
        while (currentNode is not null)
        {
            queue.Enqueue(currentNode.val);
            currentNode = currentNode.next;
        }

        return queue;
    }
}
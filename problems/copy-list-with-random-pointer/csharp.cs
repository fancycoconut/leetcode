/*
// Definition for a Node.
public class Node {
    public int val;
    public Node next;
    public Node random;
    
    public Node(int _val) {
        val = _val;
        next = null;
        random = null;
    }
}
*/

public class Solution {
    public Node CopyRandomList(Node head) {
        if (head is null) return null;
        // Key -> old node, Value => new node
        var nodeMap = new Dictionary<Node, Node>();
        var randomMap = new Dictionary<(int, int), (Node, Node)>();

        var length = 0;
        var current = head;
        var i = 0;
        while (current is not null)
        {
            nodeMap[current] = new Node(current.val);
            i++;
            length++;
            current = current.next;
        }

        Console.WriteLine(length);

        var root = nodeMap[head];
        current = head;
        var currentNew = root;
        while (current is not null)
        {
            var newNode = current.next is null
                ? null
                : nodeMap[current.next];

            if (current.random is not null && nodeMap.ContainsKey(current.random))
            {
                currentNew.random = nodeMap[current.random];
            }

            current = current.next;
            currentNew.next = newNode;   
            currentNew = currentNew.next;
        }

        return root;
    }
}
/*
// Definition for a Node.
public class Node {
    public int val;
    public IList<Node> neighbors;

    public Node() {
        val = 0;
        neighbors = new List<Node>();
    }

    public Node(int _val) {
        val = _val;
        neighbors = new List<Node>();
    }

    public Node(int _val, List<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

// Using breath first search to scan through all nodes
public class Solution {
    public Node CloneGraph(Node node) {
        if (node is null) return null;

        var queue = new Queue<Node>();
        var map = new Dictionary<int, Node>();
        var visitedNodes = new HashSet<Node>();

        queue.Enqueue(node);
        var root = new Node(node.val);
        map[node.val] = root;

        while (queue.Count > 0)
        {
            var currentNode = queue.Dequeue();
            if (visitedNodes.Contains(currentNode)) continue;

            visitedNodes.Add(currentNode);
            if (!map.ContainsKey(currentNode.val))
            {
                map[currentNode.val] = new Node(currentNode.val);
            }

            var targetNode = map[currentNode.val];
            foreach (var neighbor in currentNode.neighbors)
            {
                if (!map.ContainsKey(neighbor.val))
                {
                    map[neighbor.val] = new Node(neighbor.val);
                }

                targetNode.neighbors.Add(map[neighbor.val]);
                queue.Enqueue(neighbor);
            }
        }

        return root;
    }
}
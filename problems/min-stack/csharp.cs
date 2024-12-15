public class MinStack {
    private Node _current;

    private Node _currentMin;

    public MinStack() {
        
    }
    
    public void Push(int val) {
        if (_current is null)
        {
            _current = new Node(val);
            _currentMin = new Node(val);
            return;
        }
        
        var newNode = new Node(val);
        newNode.Prev = _current;
        _current.Next = newNode;
        _current = newNode;

        if (val <= _currentMin.Value)
        {
            var newMinNode = new Node(val);
            newMinNode.Prev = _currentMin;
            _currentMin.Next = newMinNode;
            _currentMin = newMinNode;
        }
    }
    
    public void Pop() {
        if (_current is null) return;

        if (_current.Value == _currentMin.Value)
        {
            var newMin = _currentMin.Prev;
            _currentMin = newMin;      
        }
        
        var newCurrent = _current.Prev;
        _current = newCurrent;
    }
    
    public int Top() {
        return _current.Value;
    }
    
    public int GetMin() {
        return _currentMin is null ? 0 : _currentMin.Value;
    }
}

public class Node
{
    public int Value { get; set; }
    public Node Prev { get; set; }
    public Node Next { get; set; }

    public Node(int value)
    {
        Value = value;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.Push(val);
 * obj.Pop();
 * int param_3 = obj.Top();
 * int param_4 = obj.GetMin();
 */
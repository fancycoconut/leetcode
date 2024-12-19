public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {
        var mid = matrix.Length / 2;
        var firstMatrixElement = matrix[mid][0];
        if (target > firstMatrixElement && matrix.Length > 1) return SearchMatrix(matrix[mid..], target);
        if (target < firstMatrixElement && matrix.Length > 1) return SearchMatrix(matrix[0..mid], target);
        return BinarySearch(matrix[mid], target);
    }

    private bool BinarySearch(int[] array, int target)
    {
        var mid = array.Length / 2;
        
        var current = array[mid];
        if (target > current && array.Length > 1) return BinarySearch(array[mid..], target);
        if (target < current && array.Length > 1) return BinarySearch(array[0..mid], target);

        return current == target;
    }
}
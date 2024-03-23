/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var map = {};
    for (var i = 0; i < nums.length; i++) {
      var current = nums[i];
      map[current] = i;
    }
    
    var output = [];
    for (var i = 0; i < nums.length; i++) {
      var current = nums[i];
      var complement = target - current;
      if (complement in map) {
        if (map[complement] != i) return [i, map[complement]];
        
        if (output.length == 1 && nums[output[0]] + complement != target)
          output.pop();
        else
          output.push(map[complement]);
      }
    }
    
    return output.length == 1
      ? [output[0], output[0]]
      : output;
  };
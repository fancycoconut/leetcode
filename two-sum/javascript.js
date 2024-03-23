
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

// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.

// Example 1:
// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

// Example 2:
// Input: nums = [3,2,4], target = 6
// Output: [1,2]

// Example 3:
// Input: nums = [3,3], target = 6
// Output: [0,1]
  
  /**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
  function twoSum(nums, target) {
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
  }
  
  function assertArray(expected, actual) {
    if (expected.length !== actual.length) return false;
    for (var i = 0; i < expected.length; i++) {
      if (expected[i] !== actual[i]) return false;
    }
    return true;
  }
  
  console.log("Passed: " + assertArray([0,1], twoSum([2,7,11,15], 9)));
  console.log("Passed: " + assertArray([1,2], twoSum([3,2,4], 6)));
  console.log("Passed: " + assertArray([0,1], twoSum([3,3], 6)));
  
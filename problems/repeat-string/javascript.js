/**
 * @param {number} times
 * @return {string}
 */
String.prototype.replicate = function(times) {
  var output = "";
  for (var i = 0; i < times; i++) {
      output += this;
  }

  return output;
}
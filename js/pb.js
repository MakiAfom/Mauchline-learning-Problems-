function maximumPossiblePyramidHeight(i) {
  var levelpyramid = 0;
  var cubes_used_to_build = 0;

  for (var n = 1; ; n++) {
    var cubes_vanya_needed = (n * (n + 1)) / 2;
    if (cubes_used_to_build + cubes_vanya_needed > i) {
      break;
    }
    levelpyramid++;
    cubes_used_to_build += cubes_vanya_needed;
  }

  return levelpyramid;
}

// Example usage:
const i = 10;
console.log(maximumPossiblePyramidHeight(i)); // Output: 3

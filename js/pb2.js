function maxPossibleProduct(nums, k) {
  var n = nums.length;
  const mod = Math.pow(10, 9) + 7;
  let maxProductinit = 1;

  nums.sort((x, y) => y - x);

  for (let j = 0; j < k; j++) {
    maxProductinit = (maxProductinit * nums[j]) % mod;
  }

  return maxProductinit;
}

const input = `10 3
1 2 3 4 5 6 7 8 9 10`;

const [firstInput, secondInput] = input.split("\n");
const [n, k] = firstInput.split(" ").map(Number);
const nums = secondInput.split(" ").map(Number);

console.log(maxPossibleProduct(nums, k));

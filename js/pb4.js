function findvalidIpAddresses(digits) {
  function ifisValidadress(partint) {
    if (partint.length === 0 || partint.length > 3) return false;

    if (partint.length > 1 && partint[0] === "0") return false;

    if (parseInt(partint, 10) > 255) return false;
    return true;
  }

  function backtrack(index, path) {
    if (path.length === 4) {
      if (index === digits.length) {
        result.push(path.join("."));
      }
      return;
    }

    for (let i = 1; i <= 3; i++) {
      if (index + i <= digits.length) {
        const partint = digits.slice(index, index + i).join("");
        if (ifisValidadress(partint)) {
          backtrack(index + i, [...path, partint]);
        }
      }
    }
  }

  const result = [];
  if (digits.length >= 4 && digits.length <= 12) {
    backtrack(0, []);
  }

  return [result.length, result];
}

const n = parseInt(prompt("Enter the number of digits:"));
const digits = prompt("Enter the digits separated by spaces:").split(" ");

const [count, ips] = findvalidIpAddresses(digits);

// Output
console.log(count);
ips.forEach((ips) => console.log(ips));

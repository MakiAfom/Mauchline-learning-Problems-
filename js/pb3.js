function generateComputerProblems(k, a1, x, y, m) {
  // Removed the erroneous let_number_of_problems = [n];
  var givenproblems = [a1]; // Initial problem time for the student
  for (var z = 1; z < k; z++) {
    var nextComputerProblem = (givenproblems[z - 1] * x + y) % m;
    givenproblems.push(nextComputerProblem);
  }
  return givenproblems;
}

function countInefficientProblemPairs(problems) {
  var inefficientCount = 0;
  for (let i = 1; i < problems.length; i++) {
    if (problems[i - 1][0] > problems[i][0]) {
      inefficientCount++;
    }
  }
  return inefficientCount;
}

function extractPairs(students) {
  var lines = students.trim().split("\n"); // Use .trim() to remove extra spaces
  var n = parseInt(lines[0]); // Number of students
  var allProblems = [];
  var totalProblems = 0;

  for (let i = 1; i <= n; i++) {
    var [k, a1, x, y, m] = lines[i].split(" ").map(Number);
    var problems = generateComputerProblems(k, a1, x, y, m);
    totalProblems += k;
    problems.forEach((time, index) => allProblems.push([time, i]));
  }

  allProblems.sort((a, b) => a[0] - b[0]);

  var inefficientCount = countInefficientProblemPairs(allProblems);
  console.log(inefficientCount);

  if (totalProblems <= 200000) {
    allProblems.forEach(([time, student]) => {
      console.log(time, student);
    });
  }
}

// Example Input
const students = `2
1 123 999 123 19999
1 456 1925 91285 98259128`;

extractPairs(students);

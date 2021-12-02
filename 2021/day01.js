let total = 0;
$("pre").innerText.trim().split("\n").map(el => Number(el)).reduce((prev, current) => {if (prev < current) {total += 1} return current});
console.log(total);


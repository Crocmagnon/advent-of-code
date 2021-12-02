let total = 0;
$("pre").innerText.trim().split("\n").map(el => Number(el)).map((el, index, array) => el + array[index+1] + array[index+2]).reduce((prev, current) => {if (prev < current) {total += 1} return current});
console.log(total);


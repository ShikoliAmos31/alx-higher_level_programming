#!/usr/bin/node
function add(a, b) {
	const c = a + b;
	console.log(c);
}
add(number(process.argv[2]), (number(process.argv[3])));

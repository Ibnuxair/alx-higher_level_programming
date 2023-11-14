#!/usr/bin/node

const add = (a, b) => parseInt(a) + parseInt(b);

const args = process.argv.slice(2);
const num1 = args[0];
const num2 = args[1];

if (isNaN(num1) || isNaN(num2)) {
    console.log('NaN');
} else {
    console.log(add(num1, num2));
}

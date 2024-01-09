#!/usr/bin/node

let a = Number(process.argv[2]);
console.log(a);
console.log(fact(a));
function fact(a){
    if (a === 0 || a === NaN){
        return 1;
    }
    return a * fact(a - 1);
}
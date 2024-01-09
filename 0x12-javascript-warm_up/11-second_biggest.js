#!/usr/bin/node

if (process.argv.length <= 2 || process.argv.length === 3) {
    console.log(0);
}
else {
    let integers = [];
    let j = 0;
    let largest = 0, secondLargest = 0;
    for (let i = 2; i < process.argv.length; i++) {
        integers[j] = Number(process.argv[i]);
        j++;
    }
    for (let i = 0; i < integers.length; i++) {
        if (integers[i] >= largest) {
            secondLargest = largest;
            largest = integers[i];
        }
        else if (integers[i] >= secondLargest) {
            secondLargest = integers[i];
        }
    }
    console.log(secondLargest);
}
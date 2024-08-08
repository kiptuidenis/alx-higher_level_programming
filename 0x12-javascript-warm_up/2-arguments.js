#!/usr/bin/node

const args = process.argv.slice(2);
if (args.length <= 2){
    console.log("No argument");
}
console.log('Command-line arguments', args);
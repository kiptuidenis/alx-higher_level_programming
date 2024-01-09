#!/usr/bin/node

const size = process.argv[2];

// Check if the size argument is missing or cannot be converted to an integer
if (isNaN(parseInt(size))) {
  console.log("Missing size");
} else {
  const squareSize = parseInt(size);

  for (let i = 0; i < squareSize; i++) {
    let row = '';
    for (let j = 0; j < squareSize; j++) {
      row += 'X';
    }
    console.log(row);
  }
}

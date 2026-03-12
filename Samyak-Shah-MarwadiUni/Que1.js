'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');
    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'canBorrowAllBooks' function below.
 *
 * The function is expected to return an integer (1 = true, 0 = false).
 */

function canBorrowAllBooks(copies, borrows) {            // ✅ fill function
    const events = [];

    // Reconstruct [start, end] pairs from flat array
    for (let i = 0; i < borrows.length; i += 2) {
        events.push([borrows[i], 1]);       // borrow at start
        events.push([borrows[i + 1], -1]);  // return at end
    }

    // At same time, process returns (-1) before borrows (+1)
    events.sort((a, b) => a[0] - b[0] || a[1] - b[1]);

    let active = 0;
    for (const [, event] of events) {
        active += event;
        if (active > copies) return 0;
    }
    return 1;
}

function main() {
    const copies = parseInt(readLine().trim(), 10);
    const borrowsCount = parseInt(readLine().trim(), 10);

    let borrows = [];
    for (let i = 0; i < borrowsCount; i++) {
        const borrowsItem = parseInt(readLine().trim(), 10);
        borrows.push(borrowsItem);
    }

    const result = canBorrowAllBooks(copies, borrows);
    console.log(result + '\n');
}

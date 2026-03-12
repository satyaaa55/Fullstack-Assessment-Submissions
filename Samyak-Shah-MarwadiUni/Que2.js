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
 * Complete the 'spiralTraversal' function below.
 *
 * The function is expected to return an integerArray.
 */

function spiralTraversal(mat) {                          // ✅ fill function
    const result = [];
    let top = 0, bottom = mat.length - 1;
    let left = 0, right = mat[0].length - 1;

    while (top <= bottom && left <= right) {
        // Move right
        for (let i = left; i <= right; i++) result.push(mat[top][i]);
        top++;
        // Move down
        for (let i = top; i <= bottom; i++) result.push(mat[i][right]);
        right--;
        // Move left
        if (top <= bottom) {
            for (let i = right; i >= left; i--) result.push(mat[bottom][i]);
            bottom--;
        }
        // Move up
        if (left <= right) {
            for (let i = bottom; i >= top; i--) result.push(mat[i][left]);
            left++;
        }
    }
    return result;
}

function main() {
    const matRows = parseInt(readLine().trim(), 10);
    const matColumns = parseInt(readLine().trim(), 10);

    let mat = Array(matRows);
    for (let i = 0; i < matRows; i++) {
        mat[i] = readLine().replace(/\s+$/g, '').split(' ').map(matTemp => parseInt(matTemp, 10));
    }

    const result = spiralTraversal(mat);
    console.log(result.join('\n') + '\n');
}

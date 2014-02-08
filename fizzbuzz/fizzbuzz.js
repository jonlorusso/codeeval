#!/usr/bin/env node

fs = require('fs');

function multiple(x, n) {
    return x % n == 0;
}

function fizzbuzz_str(a, b, i) {
    if (multiple(i, a)) {
        if (multiple(i, b)) {
            return "FB";
        } else {
            return "F";
        }
    } else if (multiple(i, b)) {
        return "B";
    } else {
        return i;
    }
}

function fizzbuzz(a, b, n) {
    var result = '';

    for (var i = 1; i <= n; i++) {
        result += fizzbuzz_str(a, b, i);
        if (i < n) result += ' ';
    }

    console.log(result);
}

fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line != "") {       
        line = line.replace(/\r/gm, ""); // For Windows.

        var arr = line.split(" "); // Splits the string by space
        fizzbuzz(arr[0], arr[1], arr[2]);
    }
})

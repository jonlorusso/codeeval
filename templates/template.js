#!/usr/bin/env node

var fs  = require("fs");

fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line != "") {       
        line = line.replace(/\r/gm, ""); // For Windows.

        var arr = line.split(" "); // Splits the string by space

        var diff = arr[0] - arr[1];

        console.log(diff);        
    }
})

#!/usr/bin/node
const fs = require('fs');

const [file1, file2, file3] = process.argv.slice(2);

const fileA = fs.readFileSync(file1, 'utf-8');
const fileB = fs.readFileSync(file2, 'utf-8');
const fileC = fileA + fileB;

fs.writeFileSync(file3, fileC);

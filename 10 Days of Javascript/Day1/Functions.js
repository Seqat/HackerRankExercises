'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}
/*
 * Create the function factorial here
 */
function factorial(n){
    
    var s;
    var sum=1;

    if(n ==0){
        return 1;
    }
    for(s=1;s<=n;s++){
        
        sum=sum*s;
        
    }
    return sum;
}



function main() {
    const n = +(readLine());
    
    console.log(factorial(n));
}
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
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    //Define variables
    let vowels ="";
    let consonants="";
    var i ;

    //Check everyleterin input string
    for(i=0;i< s.length;i++){
        
        //If the character is vowel, addin vowel string, 
        //else, add consonants string
        if ("aeiou".includes(s[i])){
            vowels+=s[i];
            
        }
        else{
            consonants+=s[i];
        }
    }
    // Prints the vowels
    for (i=0;i<vowels.length; i++){
        console.log(vowels[i]);
    }
    //Prints the conssonants
    for (i=0;i<consonants.length; i++){
        console.log(consonants[i]);
    }    
    
}


function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}
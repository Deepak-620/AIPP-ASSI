/**
 * Task 1: Print the first 10 natural numbers.
 * This module demonstrates a simple loop in JavaScript.
 */

function printNumbers() {
    /**
     * Print the first 10 natural numbers.
     */
    for (let i = 1; i <= 10; i++) {
        console.log(i);
    }
}

if (require.main === module) {
    printNumbers();
}
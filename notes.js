// search algorithms

// sorting algorithms

// computational algorithms

// collection algorithms


// Euclid's Algorithm
const findGCD = (a,b) => {
    while(b != 0) {
        const rem = a % b;
        a = b;
        b = rem;
    }
    return a;
};

console.log(findGCD(20, 8)); /* should be 4 */
console.log(findGCD(60, 96)); /* should be 12 */
// Reverse digits of an integer.
//
// Example1: x = 123, return 321
// Example2: x = -123, return -321

var reverse = function(x) {
    var swap = 0;
    while (x !== 0) {
        swap *= 10
        swap += x % 10;
        x = parseInt(x / 10, 10);
    }
    if (swap > Math.pow(2, 31) || swap < Math.pow(2, 31) * -1 ){
        return 0;
    }
    return swap;
};

console.log(reverse(-123456789)); //-987654321
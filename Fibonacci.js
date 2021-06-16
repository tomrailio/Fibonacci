

export default (n) => {

if (n >= 100000) {
    return -1;
}

var fibs = [];
fibs[0] = 0;
fibs[1] = 1;

for (var i = 2; i <= n; i++) {
    fibs[i] = fibs[i - 1] + fibs[i-2];
}

return fibs[n];
}

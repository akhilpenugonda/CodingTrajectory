function countBits(n) {
    const ans = [];
    for (let i = 0; i <= n; i++) {
        let count = 0;
        let num = i;
        while (num > 0) {
            count += num & 1;
            num >>= 1;
        }
        ans.push(count);
    }
    return ans;
}

/**
 * @param {number} n
 * @return {number[]}
 */

function countBits(n) {
    const ans = [];
    for (let i = 0; i <= n; i++) {
        ans.push(i.toString(2).split('1').length - 1);
    }
    return ans;
}

function countBits(num) {
    const f = new Array(num + 1).fill(0);
    for (let i = 1; i <= num; i++) {
        f[i] = f[i >> 1] + (i & 1);
    }
    return f;
}

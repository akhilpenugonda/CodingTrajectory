/**
 * @param {number[]} arr
 * @return {boolean}
 */
var checkIfExist = function(arr) {
        arr.sort((a, b) => a - b);
        let p1 = 0;
        let p2 = 1;
        while (p1 < arr.length - 1) {
            while (p2 < arr.length && arr[p2] <= arr[p1] * 2) {
                if (arr[p2] === arr[p1] * 2) {
                    return true;
                }
                p2++;
            }
            p1++;
            p2 = p1 + 1;
        }
        return false;
    };

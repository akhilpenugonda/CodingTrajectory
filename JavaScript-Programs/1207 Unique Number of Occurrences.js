/**
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function(arr) {
        let dict = {};
        for (let i of arr) {
            if (i in dict) {
                dict[i] += 1;
            } else {
                dict[i] = 1;
            }
        }

        let setTemp = new Set([0]);

        for (let v of Object.values(dict)) {
            if (setTemp.has(v)) {
                return false;
            } else {
                setTemp.add(v);
            }
        }

        return true;
    }


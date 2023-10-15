/**
 * @param {string} str
 * @return {boolean}
 */
var isValid = function(str) {
    const opening = {
        '{': '}',
        '(': ')',
        '[': ']'
    };
    const stack = [];
    for (let i = 0; i < str.length; i++) {
        if (str[i] in opening) {
            stack.push(str[i]);
        } else {
            if (opening[stack.pop()] !== str[i]) {
                return false;
            }
        }
    }
    return stack.length === 0;
};
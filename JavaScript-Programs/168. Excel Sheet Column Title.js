var convertToTitle = function(columnNumber) {
    const numberToCharacterMap = {};
    for (let i = 1; i <= 26; i++) {
        const character = String.fromCharCode(i + 64);
        numberToCharacterMap[i] = character;
    }
    let resp = "";
    while(columnNumber > 0) {
        let remainder = columnNumber % 26;
        if (remainder === 0) {
            resp = 'Z' + resp;
            columnNumber = Math.floor(columnNumber / 26) - 1;
        } else {
            resp = numberToCharacterMap[remainder] + resp;
            columnNumber = Math.floor(columnNumber / 26);
        }
    }
    return resp;
};

// var convertToTitle = function(columnNumber) {
//     if (columnNumber <= 0) return '';

//     const charCodeA = 'A'.charCodeAt(0);
//     const remainder = (columnNumber - 1) % 26;
//     const quotient = Math.floor((columnNumber - 1) / 26);

//     return convertToTitle(quotient) + String.fromCharCode(charCodeA + remainder);
// };

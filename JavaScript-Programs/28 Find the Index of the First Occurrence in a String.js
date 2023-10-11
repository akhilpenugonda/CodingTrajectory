// /**
//  * Returns the index of the first occurrence of needle in haystack,
//  * or -1 if needle is not part of haystack.
//  *
//  * @param {string} haystack - The string to search in.
//  * @param {string} needle - The string to search for.
//  * @return {number} - The index of the first occurrence, or -1 if not found.
//  */
// var strStr = function(haystack, needle) {
//     if (needle === "") return 0; // Empty needle, return 0
    
//     let p1 = 0;
//     let p2 = 0;
//     let needleLength = needle.length;
    
//     while (p1 < haystack.length) {
//         if (haystack[p1] === needle[p2]) {
//             p1++;
//             p2++;
            
//             if (p2 === needleLength) {
//                 return (p1 - needleLength);
//             }
//         } else {
//             p1++;
//             p2 = 0;
//         }
//     }
    
//     return -1; // Needle not found
// };
const strStr = (haystack, needle) => {
  if (needle === '' || needle === haystack) return 0;    // the only mandatory check here is (needle === '')
  if (haystack.length < needle.length) return -1;        // the other ones are for efficiency
  
  for (let i = 0; i < haystack.length - needle.length + 1; i++) {    // start looping through haystack until the remaining substring is shorter than needle
    if (haystack[i] === needle[0]) {                // as soon as we see a character that matches the first character of needle
      for (let j = 0; j < needle.length; j++) {     // start looping through both needle and haystack
        if (needle[j] !== haystack[i + j]) {        // as soon as the characters don't match
          break;                                    // break out of the loop and return to looping through haystack
        } else if (j === needle.length - 1){        // otherwise, if we looped through the entire needle and all of the characters matched
          return i;                                 // return the index of the first character of haystack with which we started the loop
        }
      }
    }
  }
  
  return -1;                                        // return -1 if there wasn't a match
};

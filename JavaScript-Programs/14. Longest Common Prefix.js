/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let refStr = strs[0];
    for(let str of strs)
    {
        let i = 0
        if(str.length < refStr.length && refStr.startsWith(str))
        {
            refStr = str;
        }
        while(i < str.length && i < refStr.length)
        {
            if(str[i] == refStr[i])
            {
                i++;
            }
            else
            {
                refStr = refStr.slice(0, i)
                break;
            }  
        }
    }
    return refStr;
};

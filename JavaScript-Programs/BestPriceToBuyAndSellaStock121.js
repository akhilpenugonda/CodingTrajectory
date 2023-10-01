/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    if(prices.length < 2)
    {
        return 0
    }
    let minimum = prices[0];
    let maximum = 0;
    for(let i = 0; i<prices.length; i++)
    {
        if(prices[i] < minimum)
        {
            minimum = prices[i];
        }
        if(prices[i] - minimum > maximum)
        {
            maximum = prices[i] - minimum;
        }

    }
    return maximum

};

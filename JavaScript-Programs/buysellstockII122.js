/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let N = prices.length-1;
    let i = 0;
    let buy, sell, profit = 0;
    while(i < N)
    {
        while(i < N && prices[i + 1] <= prices[i]){
            i++;
        }
        buy = prices[i];

        while(i < N && prices[i+1] >= prices[i])
        {
            i++;
        }
        sell = prices[i];

        profit += sell - buy;
    }
    return profit;
};

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buyPrice = prices[0];
        int maxProfit = 0;
        for (int dayPrice : prices) {
            if (dayPrice <= buyPrice) {
                buyPrice = dayPrice;
            }
            // profit is sell - buy
            else if (maxProfit < dayPrice - buyPrice) {
                maxProfit = dayPrice - buyPrice;
            }
        }
        return maxProfit;
    }
};

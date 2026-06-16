class Solution {
public:
    int maxProfit(vector<int>& prices) {
        return rec(prices, 0, false);
    }

private:
    int rec(vector<int>& prices, int i, bool bought) {
        if (i == prices.size()) {
            return 0;
        }
        int res = rec(prices, i + 1, bought);
        if (bought) {
            res = max(res, prices[i] + rec(prices, i + 1, false));
        } else {
            res = max(res, -prices[i] + rec(prices, i + 1, true));
        }
        return res;
    }
};
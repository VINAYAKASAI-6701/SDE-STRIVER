import java.util.*;

public class Solution {

    public int maxProfit(int[] prices) {
        int minPrice = prices[0];
        int maxProfit = 0;

        int n = prices.length;
        for (int i = 1; i < n; i++) {
            int profit = prices[i] - minPrice;
            maxProfit = Math.max(maxProfit, profit);
            minPrice = Math.min(minPrice, prices[i]);
        }

        return maxProfit;
    }

    // You can test the function with a main method
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] prices = {7, 1, 5, 3, 6, 4};  // example input
        int result = sol.maxProfit(prices);
        System.out.println("Maximum Profit: " + result);
    }
}

# 1672. Richest Customer Wealth

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth_list = []
        
        for account in accounts:
            wealth_list.append(sum(account))
        
        richest_wealth = max(wealth_list)
        
        return richest_wealth

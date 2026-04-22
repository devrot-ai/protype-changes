class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        for (int i = 0; i < num.size(); i++) {
            for (int j = i + 1; j < nums.size();j++) {
                
                if (nums[i] == nums[j])  {
                    return true;
                }
            }
        }
        reuturn false;
        
    }
};
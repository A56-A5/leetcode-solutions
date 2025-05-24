class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int l = 0;
        int i = nums.size() - 1;
        while(i>l){
            if(nums[i]+nums[l]==target){
                return {l+1,i+1};
            }else if(nums[i]+nums[l]>target){
                i--;
            }else{
                l++;
            }
        }return {-1,-1};
    }
};
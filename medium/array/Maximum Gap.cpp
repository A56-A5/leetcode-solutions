class Solution {
public:
    int maximumGap(vector<int>& nums) {
        if(nums.size() < 2) return 0; int m=0,k=0;
        sort(nums.begin(),nums.end());
        
        for(int i=1;i<nums.size();i++){
            if(nums[i-1]<nums[i]) k = nums[i] - nums[i-1];
            else if(nums[i-1]>nums[i]) k = nums[i-1] - nums[i];
            if(k>m) m = k;
        }return m;
    }
};
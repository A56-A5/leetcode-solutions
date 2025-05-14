class Solution {
public:
    bool canAliceWin(vector<int>& nums) {
        int s=0;
        int d=0;
        for(int i=0;i<nums.size();i++){
            if(nums[i] > 9) s+= nums[i];
            else d+=nums[i];
        }return !(s==d);
    }
};

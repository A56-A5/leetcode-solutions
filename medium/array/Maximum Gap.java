class Solution {
    public int maximumGap(int[] nums) {
        if(nums.length < 2) return 0; int m=0,k=0;
        Arrays.sort(nums);
        
        for(int i=1;i<nums.length;i++){
            if(nums[i-1]<nums[i]) k = nums[i] - nums[i-1];
            else if(nums[i-1]>nums[i]) k = nums[i-1] - nums[i];
            if(k>m) m = k;
        }return m;
    }
}
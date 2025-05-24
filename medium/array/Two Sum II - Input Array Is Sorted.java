class Solution {
    public int[] twoSum(int[] nums, int target) {
        int l = 0;
        int i = nums.length - 1;
        while(i>l){
            if(nums[i]+nums[l]==target){
                return new int[]{l+1,i+1};
            }else if(nums[i]+nums[l]>target){
                i--;
            }else{
                l++;
            }
        }return new int[]{-1,-1};
    }
}
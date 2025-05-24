class Solution {
    public int findFinalValue(int[] nums, int original) {
        while(true){
            int flag = 0;
            for(int i=0;i<nums.length;i++){
                if(nums[i] == original){
                    original *= 2;
                    flag = 1; break; 
                }
            }if(flag == 0) break;
        }return original;
    }
}

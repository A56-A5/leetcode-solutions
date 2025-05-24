class Solution {
    public int minMoves2(int[] nums) {
        Arrays.sort(nums);

        int c = 0;
        int x = nums[nums.length/2];

        for(int i : nums){
            c += Math.abs(x - i);
        }return c;
    }
}
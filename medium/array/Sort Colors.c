void sortColors(int* nums, int s) {
    for(int i=0;i<s;i++){
            for(int j=i;j<s;j++){
                if(nums[i]>nums[j]){
                    int temp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = temp;
                }
            }
        }
}
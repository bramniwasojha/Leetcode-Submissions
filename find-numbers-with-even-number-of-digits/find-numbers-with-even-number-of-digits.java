class Solution {
    public boolean digits(int num){
        int c=0;
        while(num>0){
            num/=10;
            c++;
        }
        return c%2==0;
    }
    public int findNumbers(int[] nums) {
        int res=0;
        for(int i=0;i<nums.length;i++){
            if(digits(nums[i])){
                res++;
            }
        }
        return res;
    }
}
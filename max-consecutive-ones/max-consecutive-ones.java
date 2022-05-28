class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int n=nums.length;
        int curr=0;
        int res=0;
        for(int i=0;i<n;i++){
            if(nums[i]==0){
                res=Math.max(res,curr);
                curr=0;
            }
            else{
                curr++;  
            }
        }
        res=Math.max(res,curr);
        return res;
    }
}
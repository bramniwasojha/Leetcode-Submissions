class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int runSum=0;
        int res=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]==1){
                runSum+=1;
            }
            else{
                if(res<runSum){
                    res=runSum;
                }
                runSum=0;    
            }
        }
        if(res<runSum){
            res=runSum;
        }
        return res;
    }
}
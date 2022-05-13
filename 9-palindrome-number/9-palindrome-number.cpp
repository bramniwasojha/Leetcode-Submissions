class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0)return false;
        long n=0;
        int num=x;
        while(true){
            n=n*10+x%10;
            x/=10;
            if(x<=0)break;
        }
        return num==n;
    }
};
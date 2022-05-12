class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        string a[indices.size()];
        string s1="";
        for(int i = 0; i < indices.size(); i++){
            a[indices[i]]=s[i];
        }
        for(int i = 0; i < indices.size(); i++){
            s1+=a[i];
        }
        return s1;
    }
};
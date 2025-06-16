class Solution {
public:
    bool digitCount(string num) {
        map<int,int>idxCount , numCount;

        for(int i=0;i<num.size();i++){
            numCount[num[i] - '0']++;
            if(num[i] != '0') idxCount[i] = (num[i] - '0');
        }return idxCount == numCount;
    }
};

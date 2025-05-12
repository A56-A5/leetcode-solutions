class Solution {
public:
    int alternateDigitSum(int n) {
        string s = to_string(n);
        int ans = 0, c = 1;
        for (char i : s) {
            ans += c * (i - '0');
            c *= -1;
        }
        return ans;
    }
};

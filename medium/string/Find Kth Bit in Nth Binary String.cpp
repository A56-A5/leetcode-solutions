class Solution {
public:
    char findKthBit(int n, int k) {
        vector<string> s(n);
        s[0] = "0";

        for (int i = 1; i < n; ++i) {
            s[i] = s[i - 1] + "1" + reverseInvert(s[i - 1]);
        }

        return s[n - 1][k - 1];
    }

private:
    string reverseInvert(const string& x) {
        string result;
        for (char c : x) {
            result += (c == '1') ? '0' : '1';
        }
        reverse(result.begin(), result.end());
        return result;
    }
};

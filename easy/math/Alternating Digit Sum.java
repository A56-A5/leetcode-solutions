class Solution {
    public int alternateDigitSum(int n) {
        String s = Integer.toString(n);
        int ans = 0, c = 1;
        for (int i = 0; i < s.length(); i++) {
            int x = s.charAt(i) - '0';
            ans += c * x;
            c *= -1;
        }
        return ans;
    }
}

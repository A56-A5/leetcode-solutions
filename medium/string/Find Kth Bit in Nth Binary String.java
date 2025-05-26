class Solution {
    public char findKthBit(int n, int k) {
        String[] s = new String[n];
        s[0] = "0";

        for (int i = 1; i < n; i++) {
            s[i] = s[i - 1] + "1" + reverseInvert(s[i - 1]);
        }

        return s[n - 1].charAt(k - 1);
    }

    private String reverseInvert(String x) {
        StringBuilder sb = new StringBuilder();
        for (char c : x.toCharArray()) {
            sb.append(c == '1' ? '0' : '1');
        }
        return sb.reverse().toString();
    }
}

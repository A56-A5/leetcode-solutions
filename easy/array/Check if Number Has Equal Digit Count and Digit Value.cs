public class Solution {
    public bool DigitCount(string num) {
        int[] count = new int[10];

        foreach (char c in num) {
            count[c - '0']++;
        }

        for (int i = 0; i < num.Length; i++) {
            int expected = num[i] - '0';
            if (count[i] != expected) {
                return false;
            }
        }

        return true;
    }
}

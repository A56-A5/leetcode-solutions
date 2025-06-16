class Solution {
    public boolean digitCount(String num) {
        int[] count = new int[10];

        for (char c : num.toCharArray()) {
            count[c - '0']++;
        }

        for (int i = 0; i < num.length(); i++) {
            int expected = num.charAt(i) - '0';
            if (count[i] != expected) {
                return false;
            }
        }

        return true;
    }
}

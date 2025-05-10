class Solution {
    public boolean isPalindrome(int x) {
        String s = String.valueOf(x);
        String r ="";
        for(int i=s.length()-1;i>=0;i--){
            r+=s.charAt(i);
        }
        if(r.equals(s)){return true;}
        return false;
    }
}

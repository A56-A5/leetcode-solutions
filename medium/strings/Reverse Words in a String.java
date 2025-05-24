class Solution {
    public String reverseWords(String s) {
        Stack<String> x = new Stack<>();
        String[] words = s.split("\\s+");
        String r="";
        for(int i=0;i<words.length;i++){
            x.push(words[i]);
            if(i!=words.length){
                x.push(" ");
            }
        }
        while(!x.isEmpty()){
            r+=x.pop();
        };
        return r.trim();
    }
}
class Solution {
    public List<List<Integer>> findMatrix(int[] nums) {
        List<Integer> n = new ArrayList<>();
        for(int num:nums){
            n.add(num);
        }List<List<Integer>> ans = new ArrayList<>();
        Set<Integer> s = new HashSet<>();
        while(!n.isEmpty()){
            List<Integer> row  = new ArrayList<>();
            for(int i=0;i<n.size();i++){
                if(!s.contains(n.get(i))){
                    s.add(n.get(i));
                    row.add(n.get(i));
                    n.remove(i);
                    i--;
                }
            }ans.add(row);
            s.clear();
        }return ans;
    }
}
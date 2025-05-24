class Solution {
    public String simplifyPath(String path) {
        var r = new ArrayList<String>();
        for(var i : path.split("/")){
            if(i.isEmpty() || i.equals(".")) continue;
            if(i.equals("..")){
                if(!r.isEmpty()){
                    r.remove(r.size()-1);
                }
            }
            else r.add(i);
        }return "/" + String.join("/",r);
    }
}
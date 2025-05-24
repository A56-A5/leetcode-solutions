class Solution(object):
    def simplifyPath(self, path):
        r = list()
        for i in path.split("/"):
            if r!=[] and i=="..":
                r.pop()
            elif i not in [".","..",""]:
                r.append(i)
        return "/"+"/".join(r)
            
        
            
            

        
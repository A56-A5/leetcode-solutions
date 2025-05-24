class Solution {
public:
    string simplifyPath(string path) {
        istringstream ss(path);
        deque<string> r;
        string i;
        string ans;
        while (getline(ss, i , '/')) {
            if (i == "." || i == "") {
                continue;
            }
            if (i == ".." && !r.empty()) {
                r.pop_front();
            } else if (i != "..") {
                r.push_front(i);
            }
        }
        while (!r.empty()) {
            ans += "/" + r.back();
            r.pop_back();
        }
        return ans.empty() ? "/": ans;
    }
};
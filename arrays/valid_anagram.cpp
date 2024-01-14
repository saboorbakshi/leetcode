#include <unordered_map>
#include <string>

using namespace std;

class Solution {
public:
    bool isAnagram1(string s, string t) {

        int len = s.length();

        if (len != t.length()) return false;

        unordered_map<char, int> ss, tt;

        for (int i = 0; i < len; ++i) {
            ss[s[i]] += 1;
            tt[t[i]] += 1;
        }

       if (ss == tt) return true;
       return false;
    }

    bool isAnagram(string s, string t) {

        if(s.size() != t.size()) return false;

        vector<int> v(26, 0);

        for(int i = 0; i < s.size(); i++){
            v[s[i] - 'a']++;
        }

        for(int i = 0; i < t.size(); i++){
            v[t[i] - 'a']--;
        }

        for(int i = 0; i < 26; i++) if(v[i] != 0) return false;

        return true;
    }
};

int main() {
    return 0;
}
#include <unordered_map>
#include <string>

using namespace std;

class Solution {
public:

    /*
    create 2 unordered maps with the key representing a char and value representing the char's frequency 
    check if associated values(frequencies) for each key(char) are the same for both maps
    time: O(n+m)
    space: O(n+m)
    */
    bool isAnagram1(string s, string t) {
        int len = s.length();

        if (len != t.length()) return false;

        unordered_map<char, int> ss, tt;

        for (int i = 0; i < len; ++i) {
            ss[s[i]] += 1;   
            tt[t[i]] += 1;   // valid for a new element in an unordered set
        }

       if (ss == tt) return true;   // operator == for unordered sets cares only about equivalence, not order
       return false;
    }

    /*
    create a vector of 26 ints, each index representing a char's positon in the alphabetical order
    for each char, increment or decrement its corresponding position in the vector
    time: O(n+m)
    space: O(26)
    */
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()) return false;

        vector<int> v(26, 0);

        for (int i = 0; i < s.size(); ++i) {
            v[s[i] - 'a']++;   // 'a' - 'a' = 0, 'z' - 'a' = 25 and so on…
        }

        for (int i = 0; i < t.size(); ++i) {
            v[t[i] - 'a']--;   
        }

        for (int i = 0; i < 26; ++i) if (v[i] != 0) return false;

        return true;
    }
};

int main() {
    return 0;
}
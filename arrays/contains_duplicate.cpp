#include <set>

using namespace std;

class Solution {
public:
    bool containsDuplicate1(vector<int>& nums) {
        set<int> myset;

        for (auto n : nums) {
            if (myset.find(n) != myset.end()) {
                return true;
            };
            myset.insert(n);
        }
        return false;
    }

    bool containsDuplicate2(vector<int>& nums) {
        int n = nums.size();

        sort(nums.begin(), nums.end());

        for (int i = 0; i < n-1; ++i) {
            if (nums[i] == nums[i+1]) {
                return true;
            }
        }
        return false;
    }
};

int main() {
    return 0;
}
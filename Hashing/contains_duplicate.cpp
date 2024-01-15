#include <set>

using namespace std;

class Solution {
public:

    /* 
    insert each item in an unordered set until you come across a previously inserted element
    time: O(n)
    space: O(n)
    */
    bool containsDuplicate1(vector<int>& nums) {
        set<int> myset;

        for (auto n : nums) {
            if (myset.find(n) != myset.end()) {   // find() returns set::end if element not found
                return true;
            };
            myset.insert(n);
        }
        return false;
    }

    /*
    sort the array, check if i and i+1 are the same or not
    time: O(nlogn)
    space: O(1)
    */
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
title:: 26. Remove Duplicates from Sorted Array

- title:: 26. Remove Duplicates from Sorted Array
- ```c++
  class Solution {
  public:
    int removeDuplicates(vector<int>& nums) {
        vector<int> nonDuplicateList;
        int cur = nums[0];
        int cnt = 1;
        
        nonDuplicateList.push_back(nums[0]);
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != cur) {
                cur = nums[i];
                nonDuplicateList.push_back(nums[i]);
                cnt++;
            }
        }
        
        nums = nonDuplicateList;
        return cnt;
    }
  };
  ```
-
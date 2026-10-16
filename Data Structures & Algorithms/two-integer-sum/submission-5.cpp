class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res;

        int apple = 0;

        // while(nums.at(j) + nums.at(k) != target){
        //     apple = nums.at(j) + nums.at(k);

        //     if (apple == target){
        //         break;
        //     }
        // }

        for(int j = 0; j < nums.size(); j++){
            for(int i = 0; i < nums.size(); i++){
                apple = nums.at(j) + nums.at(i);

                if (apple == target){
                    res.push_back(j);
                    res.push_back(i);
                    break;
                }
            }

            if (apple == target){
                    break;
            }
        }

        return res;
    }
};

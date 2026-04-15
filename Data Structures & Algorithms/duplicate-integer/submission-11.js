class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const setNums = new Set();
        for(const num of nums) {
            if (setNums.has(num)) {
                return true;
            }
            setNums.add(num);
        }
        return false;
    }
}

class Solution {
    public int search(int[] nums, int target) {
        return search(nums, target, nums.length / 2);
    }

    private int search(int[] nums, int target, int index) {
        if (index < 0 || index >= nums.length) {
            return -1;
        } else if (nums[index] == target) {
            return index;
        } else if (nums[index] > target) {
            if (index - 1 >= 0 && nums[index - 1] < target) {
                return -1;
            }
            return search(nums, target, index - 1);
        } else {
            if (index + 1 < nums.length && nums[index + 1] > target) {
                return -1;
            }
            return search(nums, target, index + 1);
        }
    }
}

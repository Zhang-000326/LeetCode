'''
    你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。

    给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。

    示例 1：

    输入：nums = [2,3,2]
    输出：3
    解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

    示例 2：

    输入：nums = [1,2,3,1]
    输出：4
    解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
         偷窃到的最高金额 = 1 + 3 = 4 。

    示例 3：

    输入：nums = [0]
    输出：0

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/house-robber-ii
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        状态：房屋序号 该房屋是否偷窃
        选择：偷 不偷
        dp[num][1] <- dp[num-1][0]+list[num]
        dp[num][0] <- max(dp[num-1][1], dp[num-1][0])
        '''
        
        nums1 = nums[:-1]
        nums2 = nums[1:]
        
        # 可以偷第一个房间，不能偷最后一个
        dp_i_1 = dp_i_0 = 0
        for i in range(len(nums1)):
            temp = dp_i_1
            dp_i_1 = dp_i_0 + nums1[i]
            dp_i_0 = max(dp_i_0, temp)
        res1 = max(dp_i_0, dp_i_1)
        # 可以偷最后一个房间，不能偷第一个
        dp_i_1 = dp_i_0 = 0
        for i in range(len(nums2)):
            temp = dp_i_1
            dp_i_1 = dp_i_0 + nums2[i]
            dp_i_0 = max(dp_i_0, temp)
        res2 = max(dp_i_0, dp_i_1)

        return max(res1,res2)
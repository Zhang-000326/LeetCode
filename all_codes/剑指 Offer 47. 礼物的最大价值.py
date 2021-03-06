'''
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

示例 1:

输入: 
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
 

提示：

0 < grid.length <= 200
0 < grid[0].length <= 200

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        '''
        每一个点的最大价值，取决于他上面和左面点的最大价值
        val_i 记录遍历每一行时的最大价值，即是当前点的左侧点的最大价值
        vals记录上一行的最大价值
        初始状态包括第一行和每一行的第一个元素
        '''
        val = 0
        vals = []
        lenth_x = len(grid)
        lenth_y = len(grid[0])
        for j in range(lenth_y):
            val += grid[0][j]
            vals.append(val)
        for i in range(1, lenth_x):
            val_i = grid[i][0] + vals[0]
            vals[0] = val_i
            for j in range(1, lenth_y):
                val_i = max(val_i, vals[j]) + grid[i][j]
                vals[j] = val_i
        return vals[lenth_y-1]
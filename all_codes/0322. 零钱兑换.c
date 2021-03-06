// 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
//如果没有任何一种硬币组合能组成总金额，返回 -1。
//
// 你可以认为每种硬币的数量是无限的。
//
// 示例 1：
//
// 输入：coins = [1, 2, 5], amount = 11
// 输出：3 
// 解释：11 = 5 + 5 + 1
//
// 示例 2：
//
// 输入：coins = [2], amount = 3
// 输出：-1
//
// 来源：力扣（LeetCode）
// 链接：https://leetcode-cn.com/problems/coin-change
// 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int min_cmp(int a, int b){
    return a>b ? b : a;
}

// 动态规划
int coinChange(int* coins, int coinsSize, int amount){
    if(coins == NULL || coinsSize == 0 || amount == 0)
        return 0;
    int* array_amount = (int*)malloc(sizeof(int)*(amount+1));
    array_amount[0] = 0;
    int i = 1, j = 0;
    for(; i <= amount; i++){
        array_amount[i] = -1;
        for(j = 0; j < coinsSize; j++){
            int derta = i - coins[j];
            if(derta < 0)
                continue;
            if(array_amount[derta] != -1){
                if(array_amount[i] == -1)
                    array_amount[i] = array_amount[derta] + 1;
                else
                    array_amount[i] = min_cmp(array_amount[i], array_amount[derta] +1);
            }   
        }
    }
    int res = array_amount[amount];
    free(array_amount);
    return res;
}
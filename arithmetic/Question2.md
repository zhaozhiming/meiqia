## 问题

一个棋盘有 8*8=64 个格子，编号 (1,1), (1,2), …… (8,8)。“马”按照“日”字走法 从指定起点跳到指定终点，写一程序求最短路径需要几步。例如，从(1,1)点跳到 (4,4)点至少要两步，一种方式为 (1,1) -> (2,3) -> (4,4)。程序接受４个 1-8 之间整 数，表示起点和终点位置，计算出最短路径需要几步。

## 解答
该程序用Java作答，源码为HorseRun.java和Point.java

## 主要思路

设置起点和重点，先根据起点查找周围“马”8个方向的点是否为终点，如果不是的话一直循环到超过边界为止，如果是的话则推出循环

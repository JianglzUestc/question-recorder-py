#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#汉诺塔问题
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
#运用递归的思路是：
#1、将前n-1个由a经c移到b（此时c是空柱）
#2、再将最下面1个由a经b移到c
#        （与b上面有n-1个不冲突，调用函数结果是直接移动print('move', a, '-->', c)）
#3、最后将n-1个由b经a移到c（此时a是空柱）

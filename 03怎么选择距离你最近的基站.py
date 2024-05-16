# -*- coding:utf-8 -*-
# @Author ：xiaonijiang 
# @Date ：2024/05/15 12:54

import math

# 基站列表，每个基站用一个二维坐标表示
stations = [(1, 3), (1, 3), (5, 6), (7, 8),(3, 4)]
# 你的位置
your_location = (0, 0)

def distance(p1, p2):
    # 计算两个点之间的距离
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def nearst_station(stations, location):
    min_distance = float('inf')
    nearst_station = None
    for station in stations:
        d = distance(station, location)
        if d < min_distance:
            min_distance = d
            nearst_station = station
    return nearst_station

print(nearst_station(stations, your_location))

"""
算法思想：
1. 定义一个函数，计算两个点之间的距离
2. 确认两个点之间距离的最小值，然后返回当前最小距离的点
"""

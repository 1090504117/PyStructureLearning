# -*- coding: UTF-8 -*-

processed = {}
processing = {}
path_nums = {}
parents = {}

graph = {}
graph["Start"] = {}
graph["Start"]["A"] = 6
graph["Start"]["B"] = 2
graph["Start"]["C"] = 3

graph["A"] = {}
graph["A"]["Fin"] = 2

graph["B"] = {}
graph["B"]["A"] = 3
graph["B"]["Fin"] = 5

graph["C"] = {}
graph["C"]["A"] = 3
graph["C"]["B"] = 1
graph["C"]["Fin"] = 3

graph["Fin"] = {}  # 终点没有邻居

def print_path(end_key):
    key = end_key
    path_str = key
    while parents.has_key(key):
        key = parents[key]
        path_str = key + '-->' + path_str
    print path_str

def find_lowest_cost_node(path_nums):
    lowest_cost_key = processing.keys()[0]
    for key, value in processing.items():
        if path_nums[key] < path_nums[lowest_cost_key]:
            lowest_cost_key = key
    return lowest_cost_key

def func(start_key, end_key):
    path_nums[start_key] = 0
    processing[start_key] = True
    lowest_cost_key = None
    while True:
        lowest_cost_key = find_lowest_cost_node(path_nums)
        if lowest_cost_key == end_key or not lowest_cost_key:
            if path_nums.has_key(end_key):
                return path_nums[end_key]
            else:
                return -1

        del processing[lowest_cost_key]
        processed[lowest_cost_key] = True
        for key, value in graph[lowest_cost_key].items():
            if not processed.has_key(key):
                processing[key] = True
                if not path_nums.has_key(key) or (path_nums[lowest_cost_key] + value) < path_nums[key]:
                    path_nums[key] = path_nums[lowest_cost_key] + value
                    parents[key] = lowest_cost_key

'''
字典用法，has_key 或者 in。None和数字要小心
改进，变换一下字典的结构
processing 与 path_nums需要分开
'''

def Test():
   print func('Start', 'Fin')
   print_path('Fin')
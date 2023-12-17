'''
作者: d233hj
创建日期: <2023-12-16  16:06:31>
最后编辑时间: <2023-12-16  16:58:29>
最后编辑人员: d233hj
FilePath: \worldTree\test.py
'''
from tool.AdbTool import AdbTool
from mod.WorldTree import WorldTree
import cv2


def test1():
    xuanze = cv2.imread("./img/xuanze.png")
    adbTool = AdbTool()
    adbTool.apper_to_click(xuanze)
    if (adbTool.getMsg != "None"):
        print(adbTool.getMsg())


def test2():
    world_tree = WorldTree()
    world_tree.goto_maoxian(3, True)
    while world_tree.goto_qiyu(1):
        pass
    else:
        world_tree.quit_maoxian()

"""
从此处运行脚本
"""
try:
    i = 0
    while i < 1000:
        test2()
        i = i + 1
except BaseException as e:
    pass

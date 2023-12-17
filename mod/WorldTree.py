import os
import cv2
from PIL import Image
import time
from tool.AdbTool import AdbTool

adbTool = AdbTool()
print(adbTool.getMsg())


class WorldTree:
    '''
    世界树操作类
    '''

    def __init__(self):
        self.__fight_time = 0
        self.__pageBefore = ""

    def goto_maoxian(self, nandu=1, skip_set_kuaisuzhandou=False):
        """
        来到冒险界面
        nandu:默认值1， 可选值：1，3， 代表难度 1和 3
        skip_set_kuaisuzhandou:默认值False，将不会跳过对 快速战斗 和 跳过编队 的打勾
        """
        chufamaoxian = cv2.imread("./img/chufamaoxian.png")
        shexian = cv2.imread("./img/shexian.png")
        sijing = cv2.imread("./img/sijing.png")
        kaishibiaoyan = cv2.imread("./img/kaishibiaoyan.png")

        maoxianzhong = cv2.imread("./img/maoxianzhong.png")
        maoxianzhong1 = cv2.imread("./img/maoxianzhong1.png")
        kuaishanbianyan = cv2.imread("./img/kuaishanbiaoyan.png")
        tiaoguobiandui = cv2.imread("./img/tiaoguobiandui.png")
        if nandu == 1:
            nandu = shexian
        elif nandu == 3:
            nandu = sijing
        while 1:
            "进入冒险界面"
            self.__pageBefore = "None"

            if adbTool.apper_to_click(kaishibiaoyan):
                self.__pageBefore = "kaishibiaoyan"
                continue
            if adbTool.apper_to_click(nandu):
                self.__pageBefore = nandu
                continue
            if adbTool.apper_to_click(chufamaoxian):
                self.__pageBefore = "chufamaoxian"
                continue

            # end
            if adbTool.research_img(maoxianzhong):
                self.__pageBefore = "maoxianzhong"
                break
            print("#-False:" + self.__pageBefore)
        while not skip_set_kuaisuzhandou:
            "调整快速战斗设置"
            if adbTool.apper_to_click(kuaishanbianyan):
                time.sleep(0.2)
                continue
            if adbTool.apper_to_click(tiaoguobiandui):
                time.sleep(0.2)
                continue

            if adbTool.research_img(maoxianzhong1):
                self.__pageBefore = "maoxianzhong1"
                break
            print("#-False:" + self.__pageBefore)

    def __zhandou(self):
        """
        进入战斗后的处理函数
        目标是处理从开始战斗到回到冒险界面的所有情况
        ！只完成了部分简单情况的处理
        """
        zhandouzhong = cv2.imread('./img/zhandouzhong.png')
        zhandouwancheng = cv2.imread('./img/zhandouwancheng.png')
        jiesuan = cv2.imread('./img/jiesuan.png')
        huodedaoju = cv2.imread('./img/huodedaoju.png')
        jiacheng = cv2.imread('./img/jiacheng.png')
        sure = cv2.imread("./img/sure.png")
        xuanze = cv2.imread("./img/xuanze.png")
        while 1:
            if adbTool.research_img(zhandouzhong):
                continue
            if adbTool.apper_to_click(zhandouwancheng):
                continue
            if adbTool.apper_to_click(jiesuan):
                break
        while 1:
            if adbTool.apper_to_click(xuanze):
                continue
            if adbTool.apper_to_click(huodedaoju):
                continue
            if adbTool.apper_to_click(jiacheng):
                pass
            if adbTool.apper_to_click(sure):
                break

    def goto_next_card(self):
        """
        前往下一张卡面
        处理所有类型的卡面
        ！由于没写完，只能处理“普通战斗”
        """
        chufamaoxian = cv2.imread('./img/chufamaoxian.png')
        loading = cv2.imread('./img/loading.png')
        kaishibiaoyan = cv2.imread("./img/kaishibiaoyan.png")
        qiyu = cv2.imread("./img/qiyu.png")
        xiuxi = cv2.imread("./img/xiuxi.png")
        tuzishangdian = cv2.imread("./img/tuzishangdian.png")
        huode = cv2.imread("./img/huodedaoju.png")
        baoxiang = cv2.imread("./img/baoxiang.png")
        zhanbu = cv2.imread("./img/zhanbu.png")
        zhandou = cv2.imread("./img/zhandou.png")
        zhandou1 = cv2.imread("./img/zhandou1.png")
        zhandou2 = cv2.imread("./img/zhandou2.png")
        shezhi = cv2.imread("./img/shezhi.png")
        fangqizhandou = cv2.imread("./img/fangqizhandou.png")
        fangqi = cv2.imread("./img/fangqi.png")
        xuanze = cv2.imread("./img/xuanze.png")
        sanxuan = cv2.imread("./img/sanxuanze.png")
        jiesugoumai = cv2.imread("./img/jiesugoumai.png")
        sure = cv2.imread("./img/sure.png")
        nSure = cv2.imread("./img/nSure.png")
        while 1:
            if adbTool.apper_to_click(zhandou):
                self.__zhandou()
                break
            if adbTool.apper_to_click(zhandou1):
                self.__zhandou()
                break
            if adbTool.apper_to_click(zhandou2):
                self.__zhandou()
                break

            if adbTool.apper_to_click(zhandou):
                print("没有战斗！")
                break

    def __xiuxi(self):
        self.__qiyu()

    def __qiyu(self, check_nums=1):
        """
        解决奇遇中遇到的事件，回到冒险界面
        """
        xuanze = cv2.imread("./img/xuanze.png")
        sanxuan = cv2.imread("./img/sanxuanze.png")
        fangqi = cv2.imread("./img/fangqi.png")
        shuangxuan = cv2.imread("./img/shuangxuanze.png")
        maoxianzhong = cv2.imread("./img/maoxianzhong.png")
        huodedaoju = cv2.imread("./img/huodedaoju.png")
        shezhi =cv2.imread("./img/shezhi.png")

        while 1:
            if adbTool.apper_to_click(shezhi):
                return False
            if adbTool.apper_to_click(fangqi):
                continue
            if adbTool.apper_to_click(shuangxuan):
                continue
            if adbTool.apper_to_click(sanxuan):
                continue
            if adbTool.apper_to_click(xuanze):
                continue
            if adbTool.apper_to_click(huodedaoju):
                continue

            if adbTool.research_img(maoxianzhong):
                check_nums = check_nums - 1
                if check_nums > 0:
                    continue
                print("完成奇遇！")
                return True

    def quit_maoxian(self):
        """
        从冒险界面退出，回到进入冒险前的界面
        """
        quit = cv2.imread("./img/quit.png")
        exit = cv2.imread("./img/exit.png")
        queren = cv2.imread("./img/queren.png")
        maoxianjiesuan = cv2.imread("./img/maoxianjiesuan.png")

        chufamaoxian = cv2.imread("./img/chufamaoxian.png")

        while 1:
            if adbTool.apper_to_click(maoxianjiesuan):
                continue
            if adbTool.apper_to_click(queren):
                continue
            if adbTool.apper_to_click(exit):
                continue
            if adbTool.apper_to_click(quit):
                continue

            if adbTool.research_img(chufamaoxian):
                break

    def goto_qiyu(self, check_nums):
        """
        只打奇遇，没有就走
        check_nums: 尝试寻找奇遇的次数
        return: True     进入奇遇
                False    没有找到奇遇
        遇到奇遇将调用 worldTree.__qiyu
        将回到冒险界面
        """
        qiyu = cv2.imread("./img/qiyu.png")
        qiyu1 = cv2.imread("./img/qiyu1.png")
        qiyu2 = cv2.imread("./img/qiyu2.png")
        xiuxi = cv2.imread("./img/xiuxi.png")
        fangqizhandou = cv2.imread("./img/fangqizhandou.png")

        maoxianzhong = cv2.imread("./img/maoxianzhong.png")
        assert 0 < check_nums < 1024
        while 1:
            if adbTool.apper_to_click(qiyu):
                if self.__qiyu():
                    return True
                else:
                    while 1:
                        if adbTool.apper_to_click(fangqizhandou):
                            return False
            if adbTool.apper_to_click(qiyu1):
                if self.__qiyu():
                    return True
                else:
                    while 1:
                        if adbTool.apper_to_click(fangqizhandou):
                            return False
            if adbTool.apper_to_click(qiyu2):
                if self.__qiyu():
                    return True
                else:
                    while 1:
                        if adbTool.apper_to_click(fangqizhandou):
                            return False
            if adbTool.apper_to_click(xiuxi):
                if self.__qiyu():
                    return True
                else:
                    while 1:
                        if adbTool.apper_to_click(fangqizhandou):
                            return False

            if adbTool.research_img(maoxianzhong):
                check_nums = check_nums - 1
                if check_nums > 0:
                    continue
                print("没有奇遇！")
                return False

# -*- coding: utf-8 -*-

################################################################################
## Github:http://github.com/funny-geek/Random-Selection
## Gitee:http://gitee.com/funny-geek/Random-Selection
## day 7:my first program finish
## by 稽术宅(funny-geek)
## 2022-01-04
## V1.0
################################################################################


from PySide2.QtWidgets import QMessageBox

# 导入模块 #
import random


class Selection:
    ## 以下为随机选择的过程代码 ##

    # 定义函数 #

    # 读取list.txt总文本
    def Read_List():
        try:
            with open("list.txt", "r", encoding="utf-8") as TXT_File:
                TEMP0 = TXT_File.readlines()
            TEMP2 = [TEMP1.strip() for TEMP1 in TEMP0 if TEMP1.strip("\n") != ""]
            return TEMP2
        except:
            try:
                with open("list.txt", "r", encoding="gbk") as TXT_File:
                    TEMP0 = TXT_File.readlines()
                TEMP2 = [TEMP1.strip() for TEMP1 in TEMP0 if TEMP1.strip("\n") != ""]
                return TEMP2
            except:
                print(
                    "错误 - Error：\n程序运行时遇到了错误，以下是常见的原因：\n1.“list.txt”文件不存在\n2.代码运行路径不正确\n3.“list.txt”使用了不支持的文件编码（仅支持GBK和UTF-8）\n\nThe program encountered errors while running,the following are common reasons:\n1. The \"list.txt\" file does not exist\n2. The code running path is incorrect\n3. \"list.txt\" uses unsupported file encoding (Only GBK and UTF-8 are supported)."
                )
                QMessageBox.critical(
                    None,
                    "错误 - Error",
                    "程序运行时遇到了错误，以下是常见的原因：\n1.“list.txt”文件不存在\n2.代码运行路径不正确\n3.“list.txt”使用了不支持的文件编码（仅支持GBK和UTF-8）\n\nThe program encountered errors while running,the following are common reasons:\n1. The \"list.txt\" file does not exist\n2. The code running path is incorrect\n3. \"list.txt\" uses unsupported file encoding (Only GBK and UTF-8 are supported).",
                    QMessageBox.Ok,
                )
                quit()

    # 根据list.txt文本有效行数生成随机数
    def Random_Lines():
        global Random_NUM
        Random_NUM = random.randint(1, len(Selection.Read_List()))

    # 读取设置文件文本

    # 读取不被选择的内容no_choice.txt
    def Settings_Not_Choice():
        try:
            with open(
                "./data/settings/no_choice.txt", "r", encoding="utf-8"
            ) as TXT_File:
                TEMP0 = TXT_File.readlines()
            TEMP2 = [TEMP1.strip() for TEMP1 in TEMP0 if TEMP1.strip("\n") != ""]
            return TEMP2
        except:
            try:
                with open(
                    "./data/settings/no_choice.txt", "r", encoding="gbk"
                ) as TXT_File:
                    TEMP0 = TXT_File.readlines()
                TEMP2 = [TEMP1.strip() for TEMP1 in TEMP0 if TEMP1.strip("\n") != ""]
                return TEMP2
            except:
                print(
                    "错误 - Error：\n程序运行时遇到了错误，以下是常见的原因：\n1.“./data/settings/no_choice.txt”文件不存在\n2.“./data/settings/no_choice.txt”使用了不支持的文件编码（仅支持GBK和UTF-8）\n\nThe program encountered errors while running,the following are common reasons:\n1. The \"./data/settings/no_choice.txt\" file does not exist\n2. \"./data/settings/no_choice.txt\" uses unsupported file encoding (Only GBK and UTF-8 are supported)."
                )
                QMessageBox.critical(
                    None,
                    "错误 - Error",
                    "程序运行时遇到了错误，以下是常见的原因：\n1.“./data/settings/no_choice.txt”文件不存在\n2.“./data/settings/no_choice.txt”使用了不支持的文件编码（仅支持GBK和UTF-8）\n\nThe program encountered errors while running,the following are common reasons:\n1. The \"./data/settings/no_choice.txt\" file does not exist\n2. \"./data/settings/no_choice.txt\" uses unsupported file encoding (Only GBK and UTF-8 are supported).",
                    QMessageBox.Ok,
                )
                quit()

    # 读取降低概率的内容reduced_pr.txt
    def Settings_Reduced_Pr():
        try:
            with open(
                "./data/settings/reduced_pr.txt", "r", encoding="utf-8"
            ) as TXT_File:
                TEMP0 = TXT_File.readlines()
            TEMP2 = [TEMP1.strip() for TEMP1 in TEMP0 if TEMP1.strip("\n") != ""]
            return TEMP2
        except:
            try:
                with open(
                    "./data/settings/reduced_pr.txt", "r", encoding="gbk"
                ) as TXT_File:
                    TEMP0 = TXT_File.readlines()
                TEMP2 = [TEMP1.strip() for TEMP1 in TEMP0 if TEMP1.strip("\n") != ""]
                return TEMP2
            except:
                print(
                    "错误 - Error：\n程序运行时遇到了错误，以下是常见的原因：\n1.“./data/settings/reduced_pr.txt”文件不存在\n2.“./data/settings/reduced_pr.txt”使用了不支持的文件编码（仅支持GBK和UTF-8）\n\nThe program encountered errors while running,the following are common reasons:\n1. The \"./data/settings/reduced_pr.txt\" file does not exist\n2. \"./data/settings/reduced_pr.txt\" uses unsupported file encoding (Only GBK and UTF-8 are supported)."
                )
                QMessageBox.critical(
                    None,
                    "错误 - Error",
                    "程序运行时遇到了错误，以下是常见的原因：\n1.“./data/settings/reduced_pr.txt”文件不存在\n2.“./data/settings/reduced_pr.txt”使用了不支持的文件编码（仅支持GBK和UTF-8）\n\nThe program encountered errors while running,the following are common reasons:\n1. The \"./data/settings/reduced_pr.txt\" file does not exist\n2. \"./data/settings/reduced_pr.txt\" uses unsupported file encoding (Only GBK and UTF-8 are supported).",
                    QMessageBox.Ok,
                )
                quit()

    # 执行随机选取
    def Random_Selection():
        Selection.Read_List()  # 读取list.txt总文本

        # 检查文本行数是否合法
        if len(Selection.Read_List()) < 1:
            print(
                "警告 - Warning：\n请填写随机选择列表，当前list.txt有效文本行数小于1！\nPlease fill in the random selection list, the list.txt the number of valid text lines is less than 1."
            )
            QMessageBox.warning(
                None,
                "警告 - Warning",
                "请填写随机选择列表，当前list.txt有效文本行数小于1！\nPlease fill in the random selection list, the list.txt the number of valid text lines is less than 1.",
                QMessageBox.Ok,
            )
            quit()
        if len(Selection.Read_List()) == 1:
            print(
                "警告 - Warning：\n随机列表有效结果应大于2，当前list.txt可用文本行数等于1\nThe valid result of random list should be greater than 2, list.txt the number of lines of available text is equal to 1."
            )
            QMessageBox.warning(
                None,
                "警告 - Warning",
                "随机列表有效结果应大于2，当前list.txt可用文本行数等于1\nThe valid result of random list should be greater than 2, list.txt the number of lines of available text is equal to 1.",
                QMessageBox.Ok,
            )
            quit()

        # 根据list.txt文本总行数生成随机数
        Selection.Random_Lines()

        # 输出结果
        print("随机数结果：", Random_NUM)
        for Print_Not_Choice in Selection.Settings_Not_Choice():
            print("不被选内容：", Print_Not_Choice)
        print("随机行文本：", Selection.Read_List()[Random_NUM - 1])
        print("不选内容数：", len(Selection.Settings_Not_Choice()))

        # 判断随机行文本中是否包含降低概率的内容
        for TEMP0 in Selection.Settings_Reduced_Pr():  # 当前选择的内容逐一匹配不可选取的列表中的内容
            if TEMP0 in Selection.Read_List()[Random_NUM - 1]:  # 如果当前选择的内容包含不可选取的列表中的内容
                Selection.Random_Lines()  # 重新生成随机内容
                print("--已重选--")
                print("新的随机数：", Random_NUM)
                print("新随机文本：", Selection.Read_List()[Random_NUM - 1])
                # 效果：实际选中概率为原概率的平方(例：(1/2)^2=1/4)

        # 判断随机行文本中是否包含不选取的内容
        Count_NUM = 1  # 循环计数变量
        Error_Count = 0  # 死循环检测变量
        while Count_NUM <= len(
            Selection.Settings_Not_Choice()
        ):  # 在当前选择的内容不包含所有不可选取的内容之前一直循环
            Count_NUM = 1
            Error_Count += 1
            if Error_Count >= 1000:  # 死循环检测
                print(
                    "错误 - Error：\n程序疑似进入死循环，已为您终止程序！请检查list.txt和设置文件配置！\nThe program is suspected to have entered an endless cycle, and the program has been terminated for you! Please check the list.txt and settings file configuration."
                )
                QMessageBox.critical(
                    None,
                    "错误 - Error",
                    "程序疑似进入死循环，已为您终止程序！请检查list.txt和设置文件配置！\nThe program is suspected to have entered an endless cycle, and the program has been terminated for you! Please check the list.txt and settings file configuration.",
                    QMessageBox.Ok,
                )
                quit()
            for TEMP0 in Selection.Settings_Not_Choice():  # 当前选择的内容逐一匹配不可选取的列表中的内容
                if (
                    TEMP0 in Selection.Read_List()[Random_NUM - 1]
                ):  # 如果当前选择的内容包含不可选取的列表中的内容
                    Selection.Random_Lines()  # 重新生成随机内容
                    print("-已重新选择-")
                    print("新的随机数：", Random_NUM)
                    print("新随机文本：", Selection.Read_List()[Random_NUM - 1])
                    break  # 重设数值，重新检查
                Count_NUM += 1

        # 输出结果
        print("----------")
        print("最终随机文本：", Selection.Read_List()[Random_NUM - 1])
        return Selection.Read_List()[Random_NUM - 1]

    ## 以上为随机选择的过程代码 ##

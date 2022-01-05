# 随机选择(课堂点名器) Random-Selection

这是一个随机选择器(课堂点名器)，老师可以用它随机点名一个同学在课堂上回答问题(当然有后门让它不点你的名字)，或者用它来解决你的选择困难症
This is a random selector (roll call device), which can be used by teachers to choose a random classmate to answer questions in class (of course, it has a back door, so you can make it not choose you), or use it to solve your choice difficulty.

这是一个Python初学者（学了七天）的作品
This is the work of a Python beginner (seven days of study)

## 文件说明 Document description

### list.txt
在里面填入需要选择的内容，每行一个，允许空行，但是空行不会被选择(如果有特别需求，允许空格)，不过这样做会降低软件运行效率，不建议超过500条
Fill in the content that needs to be selected, one per line, allow blank lines, but blank lines will not be selected (if there are special requirements, spaces can be used), and this will reduce the efficiency of software operation, it is not recommended to exceed 500.

### ./data/setting/no-choice.txt
在这里填写关键词，每行一个，“list.txt”中包含对应关键词的内容所在的行将不会被选择，不建议超过50条。
Fill in keywords here, one for each line, and the line containing the content of the corresponding keyword in "list.txt" will not be selected, it is not recommended to exceed 50.

### ./data/setting/reduced_pr.txt
在这里填写关键词，每行一个，“list.txt”中包含对应关键词的内容所在的行将会降低被选择的概率，不建议超过50条
Fill in the keywords here, one for each line. The row containing the content of the corresponding keyword in "list.txt" will reduce the probability of being selected, it is not recommended to exceed 50.

## 其他特性 Other features:

允许手动直接修改GUI程序中标签的内容，可以拿来开玩笑（程序存在一定问题，部分内容可能无法直接输入，但是可以通过复制粘贴的方式输入）
Allow manual direct modification of the content of the table in the GUI program, which can be used as a joke (the program has some problems, some of the content may not be entered directly, but can be entered by copy and paste)

允许修改位于“./data/img/WindowIcon.ico”的图标文件
Allows to modify the icon file located in ". /data/img/WindowIcon.ico" icon file.

充足的中文注释，适合Python初学者学习
Sufficient Chinese comments, suitable for Python beginners.

### 此项目可能不会再更新 This project may not be updated again

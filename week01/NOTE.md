第一周学习笔记：
1、学习思维导图见week0Node.png

问题：

1、在parse函数中使用yield调用parse2会查找不到对应的内容，把parse2的调用放在start_requests却可以正常读取到，麻烦抽时间帮忙看下代码，代码已上传到作业下面，多谢了！

2、使用scrapy框架时，我在开头加入了如下代码：
`import sys
sys.path.append("D:\\user\\pys\\Python-002\\")
print(f"current path:{sys.path}")`
防止路径的问题，这个和pycharm感觉是冲突的，有没什么好的办法？

3、使用scrapy框架时如何断点调试，我现在运行后是通过print和日志来看问题的，对于数据的调试不是很方便，是否有更好的方法？
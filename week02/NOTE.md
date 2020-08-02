学习笔记:
见同目录下的图片

学习问题：
1、在使用如下语句爬取到的数据是一个包含了“\r\n、空格”的list：
`movie_type = movie_info.xpath("./div[contains(@class,'movie-hover-title')]/text()")`

我是使用
`movie_tag = list(filter(lambda x: x != '', [item.strip() for item in movie_type.extract()]))`解决的

经过查询资料，有一个normalize-space函数，但该函数对list并没有作用，麻烦问下有没更好的方法？

2、我把查询语句也放入了pipelines内，由于yield的原因，会查询10次，
按照我的理解查询数据也应该是在管道中进行获取，但只需要获取一次就可以了，请问该如何定义函数才可以自动执行？
其实，主要是不清楚在pipeline中如何标准定义函数？以及对应的执行逻辑是什么？
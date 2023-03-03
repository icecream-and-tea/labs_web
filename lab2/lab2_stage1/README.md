![](.\img\关系图.png)

*`my_statistics.py`用于统计子图中的实体和关系数量*



本实验就是在已有的图上进行搜寻（search）和过滤（filter）得到两跳子图。整体关系如上图。

需要注意的点有以下几个：

- 因为`freebase_doban.gz`与`origin_graph_step2.txt.gz`过大不在此文件夹中。前者可以通过助教云盘下载，后者需要自己跑程序得到。
- 运行`searcher1.py`和`searcher2.py`所需时间均在10min以上

- 虽然一跳二跳子图文件都是三元组文件，但最开始的一跳未筛选子图有网页前缀（http://rdf.freebase.com/ns），后面的没有。这是前后设计不一致导致的，无伤大雅。
- 关于实体出现m次，关系出现n次的筛选条件请注意同时筛选和先后筛选有很大的差别。因为当你通过**实体次数**筛选得到一个图后，需要对**关系**在**这个图而不是筛选之前原来的图**进行重新的统计。
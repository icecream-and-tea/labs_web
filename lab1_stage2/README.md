# Stage2: search engine

## 目录结构

* `parser_books.py, parser_movies.py`分别是对书籍，电影进行分词的程序。
* `info_book.json, info_movie.json`分别是stage1爬取的书籍与电影信息。
* `words_books.json, words_movies.json`是分词之后的结果。
* `stop_words_books.json, stop_words_movies.json`是分词过程中使用的停用词，由于内容偏向性不同，两个文件有少量词语存在差别。
```
.
├── README.md                            ---> 你在这里
├── doc
│   ├── Book_tag.csv                     ---> 助教给的词库
│   ├── Movie_tag.csv                   
│   ├── new_book_id.txt                  ---> 通过爬取的数据生成的新的id-num文档
│   ├── new_movie_id.txt
│   ├── posting_list_books.json          ---> 根据分词结果构造的倒排表(通过dic嵌套list实现)
│   ├── posting_list_movies.json
│   ├── stop_words_books.json            ---> 停用词表
│   ├── stop_words_movies.json
│   ├── words_books.json　　　　　　　　 ---> 分词结果
│   └── words_movies.json
└── src
    ├── new_label.py                     ---> 处理新标签
    ├── parser_books.py                  ---> 分词程序
    ├── parser_movies.py
    ├── posting_list_book.py             ---> 倒排表程序
    └── posting_list_movies.py
```

## 分词使用到的库或工具包

* 分词程序运行在python3.10版本上，需要安装[pkuseg分词工具](https://github.com/lancopku/pkuseg-python)。
* 停用词在[中文常用停用词表](https://github.com/goto456/stopwords/blob/master/cn_stopwords.txt)的基础上，针对所爬取的内容，添加了一些词语。

## 构建倒排表
* 前置操作：

	通过 stage 1 爬出来的数据建立`new_***_id.txt`，此时保存了`id_num_list[]`以供后续程序使用。

* 倒排表结构：

	```python
	dic = {
	    key1: [n1, ...],
	    key2: [n2, ...],
	    ...
	}
	```

* 构建倒排表：
	* 根据分词结果，遍历`words_***.json`文件，将分词加入到`dic`的关键词`key`中。对于每个关键词`key`，`value`值为所有出现该分词的`id`对应的`num`的列表。
	* 对于每个关键词`key`后的列表，利用`sort()`升序排列以便构造跳表。
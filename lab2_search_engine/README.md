# Stage2: search engine

## 目录结构

* `parser_books.py, parser_movies.py`分别是对书籍，电影进行分词的程序。
* `info_book.json, info_movie.json`分别是stage1爬取的书籍与电影信息。
* `words_books.json, words_movies.json`是分词之后的结果。
* `stop_words_books.json, stop_words_movies.json`是分词过程中使用的停用词，由于内容偏向性不同，两个文件有少量词语存在差别。

## 使用到的库或工具包

* 分词程序运行在python3.10版本上，需要安装[pkuseg分词工具](https://github.com/lancopku/pkuseg-python)。
* 停用词在[中文常用停用词表](https://github.com/goto456/stopwords/blob/master/cn_stopwords.txt)的基础上，针对所爬取的内容，添加了一些词语。


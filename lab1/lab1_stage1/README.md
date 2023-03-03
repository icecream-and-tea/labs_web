```
.
|-- README.md                             ---> 你在这里
|-- book_spider                           ---> 书籍相关的代码
|   |-- doc                               
|   |   |-- Book_id.txt                   ---> 要爬取的书籍id					
|   |   |-- json
|   |       `-- info_book.json            ---> 最终解析之后的信息
|   `-- src
|       |-- bucket.py					  ---> 无需关注
|       |-- fake_useragent.py             ---> 用户代理池
|       |-- html_parser.py                ---> 页面解析器，对爬下来的源码解析
|       |-- index.py                      ---> 主程序
|       `-- spider.py                     ---> 爬虫
`-- movie_spider                          ---> 电影相关的代码
    |-- doc                               ---> 和书籍的一样，不再注释
    |   |-- Movie_id.txt
    |   `-- json
    |       `-- info_movie.json
    `-- src
        |-- bucket.py
        |-- fake_useragent.py
        |-- html_parser.py
        |-- index.py
        `-- spider.py
```


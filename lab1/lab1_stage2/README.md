# Stage2: search engine

## 目录结构

```
.
|-- README.md                            ---> 你在这里
|-- __init__.py                          ---> 没写，也没用
|-- books                                ---> 书籍相关的代码
|   |-- doc                              
|   |   |-- Book_tag.csv                 ---> 新的tag
|   |   |-- new_books_id.txt             ---> 去除坏结点的电影id列表
|   |   |-- no_syn_words_books.json      ---> 经过去停用词，合并近义词的分词结果
|   |   |-- posting_list_books.json      ---> 书籍的倒排表
|   |   |-- stop_words_books.json        ---> 书籍的停用词表
|   |   |-- syno_dict_books.json         ---> 书籍的同近义词表
|   |   `-- words_books.json             ---> 最原始的分词结果
|   `-- src
|       |-- parser_books.py              ---> 对书籍信息进行分词
|       `-- posting_list_book.py         ---> 建立倒排表的
|-- common
|   |-- bool_inquire                     ---> 处理用户输入，显示最终结果
|   |   |-- compress.py                  ---> 对压缩后的倒排表解码
|   |   |-- main.py                      ---> 主程序
|   |   |-- search.py                    ---> 进行布尔查询和合并
|   |   `-- user_input_process.py        ---> 对布尔表达式预处理
|   |-- new_label.py                     ---> 加新tag的程序
|   `-- synonym
|       |-- dict_synonym.txt             ---> 最原始的同近义词表
|       |-- merge_synonym.py             ---> 进行同近义词合并
|       `-- modify_synonym_list.py       ---> 针对特定集合生成特定的同近义词表
`-- movies                               ---> 与书籍相同，不再注释
    |-- doc
    |   |-- Movie_tag.csv
    |   |-- new_movies_id.txt
    |   |-- no_syn_words_movies.json
    |   |-- posting_list_movies.json
    |   |-- stop_words_movies.json
    |   |-- syno_dict_movies.json
    |   `-- words_movies.json
    `-- src
        |-- __pycache__
        |-- parser_movies.py
        `-- posting_list_movies.py
```


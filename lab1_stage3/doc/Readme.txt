This data set was collected from Douban.com, one of the most famous Chinese SNS in China which allows users to contribute comments on movies, books, music and so on. 

Totally, this data set contains 100,176 users, 89,667 movies, and 475,820 books.

This data set was contributed by Tengfei Bao and Tong Xu from USTC, China. For using this data, please kindly cite the papers as below:

[1] Tong Xu, Hengshu Zhu, Enhong Chen, Baoxing Huai, Hui Xiong, Jilei Tian, Learning to Annotate via Social Interaction Analytics, Knowledge and Information System, 2014, 41:251-276.

[2] Tong Xu, Dong Liu, Enhong Chen, Huanhuan Cao, Jilei Tian, Towards Annotating Media Contents through Social Diffusion Analysis, In Proceedings of the 12th International Conference on Data Mining, Brussels, Belgium, 2012, 1158-1163..


Data Format Description£º
There are two kinds of data included. The file ¡°contacts.txt¡± indicates the social connections between users, while the files in folders ¡°Movie¡± and ¡°Book¡± are list of rating records.

For the file ¡°contacts.txt¡±:
Each line represents a user, which means all the IDs after colon are connected with the ID before colon.
Example: A:B,C,D means existing social connections as AB, AC and AD.
All the connections are undirected (or treated as bi-directional).

For the rating records in folders ¡°Movie¡± and ¡°Book¡±:
Each line represents a piece of rating record, in the format as:
User ID, Item (Movie/Book) ID, Rating (0-5), Timestamp[, Tag 1, Tag 2, ¡­]
Example:
A record as "1000001, 1293510,3,2005-06-26T20:41:22+08:00,black humor", indicates that user 1000001 rates the movie 1293510 as 3 stars at 2005-06-26T20:41:22+08:00, with tags ¡°black humor¡±.
All the tags are in Chinese as original. If translation is required, please feel free to contact tongxu@ustc.edu.cn.

Thanks for your attention.

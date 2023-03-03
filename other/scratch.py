import json

if __name__ == "__main__":
    infile = './lab1/lab1_stage2/movies/doc/posting_list_movies.json'
    with open(infile, encoding='UTF-8') as f_info:  # 加上encoding参数，否则会解码报错
        indexs = json.load(f_info)

    num = 1
    index_list = []
    for key, value in indexs.items():
        index_info = {}
        index_info["model"] = "movie_searcher.index"
        index_info["pk"] = num
        num += 1

        tmp_dict = {}
        tmp_dict["key_word"] = key
        tmp_dict["movie_list"] = value
        index_info["fields"] = tmp_dict

        index_list.append(index_info)

    with open('django_data2.json', 'w', encoding='utf-8') as outfile:
        json.dump(index_list, outfile, ensure_ascii=False, indent=1)

# if __name__ == "__main__":
#     infile = './lab1/lab1_stage1/movie_spider/doc/json/info_movie.json'
#     with open(infile, encoding='UTF-8') as f_info:  # 加上encoding参数，否则会解码报错
#         movies = json.load(f_info)
#
    # movie_list = []
    # num2 = 1
    # for num, movie in enumerate(movies):
    #     movie_info = {}
    #     movie_info["model"] = "movie_searcher.movie"
    #     movie_info["pk"] = num+1
    #
    #     tmp_dict = {}
    #     tmp_dict["title_text"] = movie['基本信息']['标题']
    #     tmp_dict["summary_text"] = movie['剧情简介']
    #     tmp_dict["comment_text"] = movie['热评']
    #     movie_info["fields"] = tmp_dict
    #
    #     movie_list.append(movie_info)
    #
    #     for celebrity in movie['演职员']:
    #         celebrity_info = {}
    #         celebrity_info["model"] = "movie_searcher.celebrity"
    #         celebrity_info["pk"] = num2
    #         num2 += 1
    #
    #         tmp2_dict = {}
    #         tmp2_dict["movie"] = num+1
    #         tmp2_dict["celebrity_text"] = celebrity[0]
    #         tmp2_dict["link"] = celebrity[2]
    #         tmp2_dict["img_link"] = celebrity[3]
    #         tmp2_dict["role"] = celebrity[1]
    #         celebrity_info["fields"] = tmp2_dict
    #
    #         movie_list.append(celebrity_info)
#
#     with open('django_data.json', 'w', encoding='utf-8') as outfile:
#         json.dump(movie_list, outfile, ensure_ascii=False, indent=1)

# [{
# 	"model": "movie_searcher.movie",
# 	"pk": 1,
# 	"fields": {
# 		"title_text": "某部电影",
# 		"summary_text": "剧情简介",
# 		"comment_text": "热评"
# 	}
# }, {
# 	"model": "movie_searcher.celebrity",
# 	"pk": 1,
# 	"fields": {
# 		"movie": 1,
# 		"celebrity_text": "某位名人",
# 		"link": "xxx",
# 		"img_link": "xxx",
# 		"role_text": "扮演某位角色"
# 	}
# }]
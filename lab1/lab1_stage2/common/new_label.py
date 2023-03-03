import json
import csv
import re

if __name__ == "__main__":
    res = list()
    error_list = list()

    movie_file = '../../lab1_spiders/movie_spider/doc/json/info_movie.json'
    with open(movie_file, encoding='utf-8') as f:
        info = json.load(f)

    label_dict = dict()
    csv_file = './doc/tag/Movie_tag.csv'
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            label_dict[row['id']] = row['tag']

    for movie_info in info:
        movie_id = movie_info['Id']
        if movie_id in label_dict:
            new_labels = label_dict[movie_id].split(',')
            movie_type = movie_info['基本信息']['类型']
            for label in new_labels:
                if label not in movie_type:
                    movie_info['基本信息']['类型'].append(label)
        res.append(movie_info)

    output = '../../lab1_spiders/movie_spider/doc/json/info_movie_test.json'
    with open(output, 'w', encoding='utf-8') as f:
        json.dump(res, f, ensure_ascii=False, indent=1)

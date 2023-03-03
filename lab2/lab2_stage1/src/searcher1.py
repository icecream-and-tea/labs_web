import gzip

# 找出所有和电影实体相关的三元组
if __name__ == "__main__":
    mid = set()
    with open('../doc/douban2fb.txt', 'r') as id_file:
        data = id_file.read().split()
    tmp = data[1::2]  # freebase中电影id
    for it in tmp:
        mid.add('<http://rdf.freebase.com/ns/' + it + '>')

    res = []  # 数据集中与mid有关的数据
    res_file = open('../doc/origin_graph_step1.txt', 'w', encoding='utf-8')
    with gzip.open('../doc/freebase_douban.gz', 'rb') as f:
        for num, line in enumerate(f):
            line = line.strip()
            triplet = line.decode().split('\t')  # triplet中0是头实体，1是关系，2是尾实体
            # if triplet[0] in mid or triplet[2] in mid:
            if triplet[0] in mid:
                res.append(triplet[0:3])
                tri_str = triplet[0] + ' ' + triplet[1] + ' ' + triplet[2] + '\n'
                res_file.write(tri_str)
            if num % 100000 == 0:
                print(num)



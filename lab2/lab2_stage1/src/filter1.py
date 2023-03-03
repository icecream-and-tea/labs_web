import re

if __name__ == "__main__":
    with open('../doc/douban2fb.txt', 'r') as id_file:
        data = id_file.read().split()
    mid = data[1::2]  # freebase中电影id

    with open('../doc/origin_graph_step1.txt', 'r', encoding='utf-8') as f:
        data = f.read()
    data = data.splitlines()

    # 最好只保留具有< http://rdf.freebase.com/ns/前缀的实体。
    # 可以过滤掉涉及三元组少于 20 个的实体，或只保留至少在 50 个三元组中出现的关系

    tri_list = []  # 三元组列表
    item_dict = {}  # 实体集合
    rela_dict = {}  # 关系集合

    # 统计实体
    for item in data:
        triplet = re.findall(re.compile(r'<http://rdf.freebase.com/ns/(.*?)>'), item)
        if len(triplet) < 3:
            continue
        # 头实体
        item_dict[triplet[0]] = 1 if triplet[0] not in item_dict else item_dict[triplet[0]]+1
        # 尾实体
        item_dict[triplet[2]] = 1 if triplet[2] not in item_dict else item_dict[triplet[2]]+1
        # 关系
        rela_dict[triplet[1]] = 1 if triplet[1] not in rela_dict else rela_dict[triplet[1]] + 1

        tri_list.append(triplet)
    print(len(item_dict))
    filter1_list = []

    # 筛选
    count = 0
    res_file = open('../doc/graph_step1.txt', 'w', encoding='utf-8')
    for triplet in tri_list:
        if item_dict[triplet[0]] > 20 and item_dict[triplet[2]] > 20 and rela_dict[triplet[1]] > 50:
            tri_str = triplet[0] + ' ' + triplet[1] + ' ' + triplet[2] + '\n'
            res_file.write(tri_str)
            count = count + 1
            print(count)

    # # 统计关系
    # rela_dict = {}  # 关系集合
    # for triplet in filter1_list:
    #     rela_dict[triplet[1]] = 1 if triplet[1] not in rela_dict else rela_dict[triplet[1]] + 1
    #
    # # 筛选关系
    # res_file = open('../doc/graph_step1.txt', 'w', encoding='utf-8')
    # for triplet in filter1_list:
    #     if rela_dict[triplet[1]] > 50:
    #         tri_str = triplet[0] + ' ' + triplet[1] + ' ' + triplet[2] + '\n'
    #         res_file.write(tri_str)

    res_file.close()

import gzip


#  对两跳子图的处理：先过滤掉出现超过 2w 次的实体和出现少于 50 次的关系；然后再采样 15 核的
#  设置，同时只保留出现大于50次的关系，对两跳子图进行清洗
if __name__ == "__main__":
    item_dict = {}
    rela_dict = {}

    print('start statistics')
    with gzip.open('../doc/origin_graph_step2.txt.gz', 'rb') as f:
        for num, line in enumerate(f):
            line = line.strip()
            triplet = line.decode().split()
            # print(triplet)
            # 头实体
            item_dict[triplet[0]] = 1 if triplet[0] not in item_dict else item_dict[triplet[0]] + 1
            # 尾实体
            item_dict[triplet[2]] = 1 if triplet[2] not in item_dict else item_dict[triplet[2]] + 1
            # 关系
            rela_dict[triplet[1]] = 1 if triplet[1] not in rela_dict else rela_dict[triplet[1]] + 1
            if num % 100000 == 0:
                print(num)

    print('start filter')
    filter_list = []
    with gzip.open('../doc/origin_graph_step2.txt.gz', 'rb') as f:
        for num, line in enumerate(f):
            line = line.strip()
            triplet = line.decode().split()
            # 高频过滤
            if item_dict[triplet[0]] < 20000 and item_dict[triplet[2]] < 20000 and rela_dict[triplet[1]] > 50:
                filter_list.append(triplet)
            if num % 100000 == 0:
                print(num)

    # 统计新的实体
    item_dict.clear()
    rela_dict.clear()
    for triplet in filter_list:
        # 头实体
        item_dict[triplet[0]] = 1 if triplet[0] not in item_dict else item_dict[triplet[0]] + 1
        # 尾实体
        item_dict[triplet[2]] = 1 if triplet[2] not in item_dict else item_dict[triplet[2]] + 1
        # 关系
        rela_dict[triplet[1]] = 1 if triplet[1] not in rela_dict else rela_dict[triplet[1]] + 1

    # 过滤实体
    res_file = open('../doc/graph_step2.txt', 'w', encoding='utf-8')
    for triplet in filter_list:
        if item_dict[triplet[0]] > 15 and item_dict[triplet[2]] > 15 and rela_dict[triplet[1]] > 50:
            tri_str = triplet[0] + ' ' + triplet[1] + ' ' + triplet[2] + '\n'
            res_file.write(tri_str)

    # 统计关系
    # rela_dict.clear()
    # for triplet in filter2_list:
    #     rela_dict[triplet[1]] = 1 if triplet[1] not in rela_dict else rela_dict[triplet[1]] + 1

    # 第二次过滤关系
    # res_file = open('../doc/graph_step2.txt', 'w', encoding='utf-8')
    # for num, line in enumerate(filter2_list):
    #     # triplet = line.split()
    #     triplet = line
    #     if rela_dict[triplet[1]] > 50:
    #         # filter2_list.append(triplet)
    #         tri_str = triplet[0] + ' ' + triplet[1] + ' ' + triplet[2] + '\n'
    #         res_file.write(tri_str)


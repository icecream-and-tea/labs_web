# 将实体和关系映射为索引值，建立一个字典，并存储到对应的文件中


if __name__ == "__main__":
    # 一、借助已有文件进行电影实体映射
    movie_id_map = {}
    with open('../doc/movie_id_map.txt', 'r') as f:
        tmp = f.read()
    tmp = tmp.split()
    for i in range(len(tmp)):
        if i % 2 == 0:
            movie_id_map[tmp[i]] = tmp[i+1]

    db_id_map = {}
    with open('../../lab2_stage1/doc/douban2fb.txt') as f:
        tmp2 = f.read()
    tmp2 = tmp2.split()
    for i in range(len(tmp2)):
        if i % 2 != 0:
            db_id_map[tmp2[i]] = tmp2[i-1]

    db_index_map = {}
    for key, value in db_id_map.items():
        db_index_map[key] = movie_id_map[value]

    print(db_index_map)

    # 二、将其余实体和关系都找出来
    with open('../../lab2_stage1/doc/graph_step2.txt', 'r') as f:
        data = f.read()
    data = data.splitlines()

    item_list = []
    rela_list = []
    triplet_list = []
    for num, line in enumerate(data):
        triplet = line.split()
        triplet_list.append(triplet)
        # 分别处理三元组中的元素
        if triplet[0] not in item_list:
            item_list.append(triplet[0])
        if triplet[2] not in item_list:
            item_list.append(triplet[2])
        if triplet[1] not in rela_list:
            rela_list.append(triplet[1])

    num = len(db_index_map)
    # 对剩余实体进行映射
    for item in item_list:
        if item not in db_index_map:
            db_index_map[item] = str(num)
            num = num+1

    rela_index_map = {}
    # 将关系进行映射
    for num, rela in enumerate(rela_list):
        rela_index_map[rela] = str(num)

    # 输出到文件中
    with open('../doc/map_item_index.txt', 'w') as f:
        for key, value in db_index_map.items():
            f.write(key + ' ' + value + '\n')

    with open('../doc/map_rela_index.txt', 'w') as f:
        for key, value in rela_index_map.items():
            f.write(key + ' ' + value + '\n')

    # 将原来的文件三元组替换
    new_triplet_list =[]
    for triplet in triplet_list:
        new_triplet = []
        new_triplet.append(db_index_map[triplet[0]])
        new_triplet.append(rela_index_map[triplet[1]])
        new_triplet.append(db_index_map[triplet[2]])
        new_triplet_list.append(new_triplet)

    # 输出到文件中
    with open('../doc/graph_step2_new.txt', 'w') as f:
        for new_triplet in new_triplet_list:
            triplet_str = new_triplet[0] + ' ' + new_triplet[1] + ' ' + new_triplet[2] + '\n'
            f.write(triplet_str)
    f.close()








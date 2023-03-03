# 统计二跳子图中实体与关系
if __name__ == "__main__":

    with open('../doc/graph_step1.txt', 'r') as f:
        data = f.read()
    data = data.splitlines()

    item_dict = {}
    rela_dict = {}
    for num, line in enumerate(data):
        triplet = line.split()
        # 头实体
        item_dict[triplet[0]] = 1 if triplet[0] not in item_dict else item_dict[triplet[0]] + 1
        # 尾实体
        item_dict[triplet[2]] = 1 if triplet[2] not in item_dict else item_dict[triplet[2]] + 1
        # 关系
        rela_dict[triplet[1]] = 1 if triplet[1] not in rela_dict else rela_dict[triplet[1]] + 1

    print(len(item_dict))
    print(len(rela_dict))
    print(len(data))


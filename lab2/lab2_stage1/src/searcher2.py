import gzip
import re

# 找出所有与一跳子图中实体相关的三元组，并在这个过程中进行频次统计
if __name__ == "__main__":
    # 统计一跳子图中的实体
    with open('../doc/graph_step1.txt', 'r') as f:
        data = f.read()
    data = data.split()

    mid = set()
    for num, item in enumerate(data):
        if num % 3 == 2 and item not in mid:
            mid.add(item)

    print(len(mid))

    # 寻找数据集中与实体相关的三元组
    res_file = gzip.open('../doc/origin_graph_step2.txt.gz', 'wb')

    with gzip.open('../doc/freebase_douban.gz', 'rb') as f:
        for num, line in enumerate(f):
            line = line.strip()
            line = line.decode()
            # triplet中0是头实体，1是关系，2是尾实体
            triplet = re.findall(re.compile(r'<http://rdf.freebase.com/ns/(.*?)>'), line)
            if len(triplet) < 3:
                continue

            # if triplet[0] in mid or triplet[2] in mid:
            if triplet[0] in mid:
                tri_str = triplet[0] + ' ' + triplet[1] + ' ' + triplet[2] + '\n'
                res_file.write(tri_str.encode())

            if num % 100000 == 0:
                print(num)

import json
import csv

if __name__ == "__main__":
    res = list()
    error_list = list()

    book_file = '../lab1_spiders/book_spider/doc/json/info_book.json'
    with open(book_file, encoding='utf-8') as f:
        info = json.load(f)

    label_dict = dict()
    csv_file = './doc/Book_tag.csv'
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            label_dict[row['id']] = row['tag']

    for book_info in info:
        book_id = book_info['Id']
        if book_id in label_dict:
            new_labels = label_dict[book_id].split(',')
            # book_type = book_info['基本信息']['类型']
            book_info['基本信息']['类型'] = new_labels
        else:
            book_info['基本信息']['类型'] = None
        res.append(book_info)

    output = '../lab1_spiders/book_spider/doc/json/info_book_test.json'
    with open(output, 'w', encoding='utf-8') as f:
        json.dump(res, f, ensure_ascii=False, indent=1)





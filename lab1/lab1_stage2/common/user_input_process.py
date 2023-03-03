# _*_ coding:utf-8 _*_
import pkuseg
import json
import merge_synonym


def not_function(input_terms):  # 处理NOT运算
    # print("not function input:")
    # print(input_terms)
    for j in range(0, len(input_terms)):  # 先对input_terms中的每个词都取反
        for i in range(0, len(input_terms[j])):
            if len(input_terms[j][i].split()) == 1:  # A => NOT A
                new_term = "NOT "
                new_term = new_term + input_terms[j][i]
                input_terms[j][i] = new_term
            else:  # NOT A => A
                input_terms[j][i] = input_terms[j][i][4:]

    output_terms = []
    for a in input_terms[0]:
        output_terms.append([a])
    place = 1
    while place < len(input_terms):
        output_temp = []
        for new_factor in input_terms[place]:
            for factor in output_terms:
                temp = factor
                temp.append(new_factor)
                output_temp.append(temp)
        output_terms = output_temp
        place = place + 1
    return output_terms


def analyse(input_string):  # 输入字符串, 输出列表形式的最小项之和
    input_string = input_string.strip()
    # print(input_string)
    if input_string[0] == "(":
        new_string = input_string[1:-1]  # 若最外侧有括号，则去掉
    else:
        new_string = input_string
    # print(new_string)

    operators = []
    not_places = []  # 保存NOT的位置
    terms_set = []
    ops = ["AND", "OR"]
    while len(new_string) > 0:
        # print("new_string:")
        # print(new_string)
        if new_string[0] != "(":
            if " " in new_string:
                single_word = new_string[0:new_string.index(" ")].strip()  # 获取第一个单词
            else:
                single_word = new_string.strip()
            # print(single_word)
            if single_word in ops:
                operators.append(single_word)
            elif single_word == "NOT":
                not_places.append(len(terms_set))
                # print(not_places)
            else:
                basic_term = [[single_word]]
                terms_set.append(basic_term)
            if " " in new_string:
                new_string = new_string[new_string.index(" "):].strip()
            else:
                new_string = ""
        else:
            temp = 1
            place = 1
            while place < len(new_string):
                if new_string[place] == "(":
                    temp = temp + 1
                elif new_string[place] == ")":
                    temp = temp - 1
                if temp == 0:
                    break
                place = place + 1
            # print("call again ")
            # print((new_string[0:place + 1]))
            terms_set.append(analyse(new_string[0:place + 1]))  # 遇到括号, 递归调用处理括号内容
            new_string = new_string[place + 1:].strip()
            # print("new_string")
            # print(new_string)
    for item in not_places:  # 首先处理NOT运算
        modified_terms = not_function(terms_set[item])
        terms_set[item] = modified_terms

    # print(terms_set)
    # print(operators)
    # print(not_places)
    if len(terms_set) != len(operators) + 1:
        print("bool expression syntax error!")
    out_put = terms_set[0]
    place = 0
    # print("out_put:")
    while place < len(operators):
        # print(out_put)
        # print(operators[place])
        terms_new = terms_set[place + 1]
        # print("terms_new")
        # print(terms_new)
        op = operators[place]
        if op == "OR":
            out_put.extend(terms_new)
        if op == "AND":
            terms_temp = []
            for term_new in terms_new:
                for term_temp in out_put:
                    temp = term_temp
                    temp = temp + term_new
                    # print(temp)
                    terms_temp.append(temp)
                    # print(terms_temp)
            out_put = terms_temp
        place = place + 1
    return out_put


def input_processor():  # 获取用户输入的布尔表达式, 输出最小项的和. 如[['A', 'NOT B'], ['C', 'D']]表示A~B+CD
    print(
        "this is a search engine about Douban books and movies, please input a bool expression consist of keywords and "
        "logical operators:)")
    print("example: 你 AND (我 OR NOT 他)")
    user_input = input(">>")
    result = analyse(user_input.strip())
    return result

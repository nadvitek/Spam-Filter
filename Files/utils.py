def read_classification_from_file(filename):
    my_dic = dict()
    with open(filename, "rt", encoding="utf-8") as f:
        for line in f:
            list_of_items = line.split()
            my_dic[list_of_items[0]] = list_of_items[1]
    return my_dic


def write_classification_to_file(file_name, dict):
    with open(file_name, 'w+', encoding='utf-8') as f:
        for key in dict:
            f.write(key + ' ' + dict[key] + '\n')


if __name__ == "__main__":
    a = read_classification_from_file("a.txt")
    print(a)

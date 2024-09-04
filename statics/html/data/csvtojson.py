import csv
import json

# 输入和输出文件的路径
csv_file_path ='./data/raw/similartips_小学.csv'
json_file_path = './data/similartips_小学.json'  # 你想要保存 JSON 数据的路径


# 读取 CSV 文件并将其转换为 JSON
data = []
with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # 将每一行的数据按照你希望的格式重新组织
        # formatted_data = {"xueshengbianhao": row["学生编号"],"shengfen": row["省份"],"chengshi": row["城市"],"nianji": row["年级"],"jiaocaibanben": row["教材版本"],"zhuceriqi": row["注册日期"] }

        # formatted_data = {"xueduan": row["学段"],"banben": row["版本"],  "jiaocaimingcheng": row["教材名称"], "danyuan": row["单元"],"cihuibianhao": row["词汇编号"], "cizubianhao": row["词组编号"], "cihui": row["词汇"], "cixing": row["词性"], "erjicixing": row["二级词性"], "ciyi": row["词义"], "zhuangtai": row["状态"]}

        # formatted_data = {"xueshengbianhao": row["学生编号"], "xueduan": row["学段"], "shoucejuanhao": row["首测卷号"], "shoucerenshicihui": row["首测认识词汇"], "shouceburenshicihui": row["首测不认识词汇"]}
        # formatted_data = {"xueshengbianhao": row["学生编号"],"chushicihuiliang": row["初始词汇量"], "chushixuexili": row["初始学习力"]}
        # formatted_data = {"xuhao": row["序号"], "xueduan": row["学段"],"dancibianhao": row["单词编号"],"danci": row["单词"],"ciyi": row["词义"]}
        #
        # formatted_data = {"xueshengbianhao": row["学生编号"], "xueduan": row["学段"], "shoucejuanhao": row["首测卷号"] , "renshi": row["首测认识词汇"],"burenshi": row["首测不认识词汇"]}
        formatted_data = {"num": row["num"],"word1": row["word1"], "word2": row["word2"], "similar": row["similar"] }

        data.append(formatted_data)

# 将 JSON 数据写入输出文件
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json_file.write("[\n")
    for i, item in enumerate(data):
        json_file.write("    " + json.dumps(item, ensure_ascii=False))
        if i < len(data) - 1:
            json_file.write(",")
        json_file.write("\n")
    json_file.write("]\n")



print(f'CSV 文件 "{csv_file_path}" 已成功转换为 JSON 文件 "{json_file_path}"')

import pandas as pd

# 从文本文件中读取数据
file_path = "C:/Users/jky/Desktop/description.txt"

with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 初始化列表以存储ID、描述和链接
ids = []
descriptions = []
links = []

# 从文本中提取ID、描述和链接
for line in lines:
    if line.startswith('ID:'):
        id = line.split(':')[1].strip()
    elif line.startswith('Description:'):
        description = line.split(':', 1)[1].strip()
    elif line.startswith('Link:'):
        link = line.split(':', 1)[1].strip()
        ids.append(id)
        descriptions.append(description)
        links.append(link)

# 使用pandas创建DataFrame
data_dict = {
    'ID': ids,
    'Description': descriptions,
    'Link': links
}
df = pd.DataFrame(data_dict)

# 将数据输出到Excel文件
output_file_path = "C:/Users/jky/Desktop/request_desc.xlsx"
df.to_excel(output_file_path, index=False)

print("数据已保存到", output_file_path)

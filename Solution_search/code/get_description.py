# function: 从description.txt中提取数据块，并将数据写入request_desc.xlsx
import re
import pandas as pd

# 读取文本文件
with open('C:/Users/jky/Desktop/description.txt', encoding='utf-8') as file:
    lines = file.read()

# 使用正则表达式匹配数据块
pattern = re.compile(r'ID: (\d+)\s+Description: ((?:(?!Link:).)*?)\s*Link: ([^\n]*?)(?=\nID:|$)', re.DOTALL)
matches = pattern.findall(lines)

data = []

# 遍历匹配结果
for match in matches:
    id = match[0]
    description = match[1]
    link = match[2]
    data.append([id, description, link])

# 创建DataFrame
df = pd.DataFrame(data, columns=['ID', 'Description', 'Link'])

# 将DataFrame写入Excel文件
excel_file_path = 'C:/Users/jky/Desktop/request_desc.xlsx'  # 设置输出文件路径
df.to_excel(excel_file_path, index=False)

print("数据已写入Excel文件:", excel_file_path)





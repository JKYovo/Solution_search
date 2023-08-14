import re

# 从文本中提取所有超链接
def extract_links(text):
    # 使用正则表达式查找匹配的超链接
    pattern = r'AddSolution\.do\?submitaction=viewsolution&fromListView=true&solutionID=\d+'
    links = re.findall(pattern, text)
    return links

with open('C:/Users/jky/Desktop/links.txt', 'r', encoding='utf-8') as file:
    text = file.read()

links = extract_links(text)

# 打印提取到的超链接
for link in links:
    print(link)

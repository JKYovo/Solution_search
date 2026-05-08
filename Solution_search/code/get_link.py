from bs4 import BeautifulSoup
import sys

file_path = sys.argv[1] if len(sys.argv) > 1 else 'data/html.txt'
output_file_path = sys.argv[2] if len(sys.argv) > 2 else 'data/links.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    html_code = file.read()

# 创建BeautifulSoup对象
soup = BeautifulSoup(html_code, 'html.parser')

# 找到所有超链接
links = soup.find_all('a')

# 去重并将提取到的超链接存储到文件
visited_links = set()
with open(output_file_path, 'w+', encoding='utf-8') as file:
    for link in links:
        link_url = link['href']
        # 去重并且写入文件
        if link_url not in visited_links:
            visited_links.add(link_url)
            file.write(link_url + '\n')

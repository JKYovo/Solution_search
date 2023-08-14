from bs4 import BeautifulSoup

# 假设您的文本内容是response_text
file_path = 'C:/Users/jky/Desktop/html.txt'  # 替换为实际的文件路径
with open(file_path, 'r', encoding='utf-8') as file:
    html_code = file.read()

# 创建BeautifulSoup对象
soup = BeautifulSoup(html_code, 'html.parser')

# 找到所有超链接
links = soup.find_all('a')

# 去重并将提取到的超链接存储到文件
visited_links = set()
output_file_path = 'C:/Users/jky/Desktop/links.txt'
with open(output_file_path, 'w+', encoding='utf-8') as file:
    for link in links:
        link_url = link['href']
        # 去重并且写入文件
        if link_url not in visited_links:
            visited_links.add(link_url)
            file.write(link_url + '\n')

count = 0

from bs4 import BeautifulSoup

# 定义函数来处理每个HTML文本段
def process_html_text(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')

    # 从'tr'元素的'data-entityid'属性中提取ID
    entity_id = soup.find('tr')['data-entityid']

    # 检查是否存在包含Description的链接元素
    description_element = soup.find('a', {'data-spa-module': 'requests', 'class': 'sb'})

    if description_element:
        # 获取包含Description的链接的title属性
        description_title = description_element['title']

        # 使用BeautifulSoup解析title属性的内容
        description_soup = BeautifulSoup(description_title, 'html.parser')

        # 提取Description文本
        description = description_soup.find('strong', string='Description :').next_sibling.strip()

        # 提取超链接
        link = description_element['href']

        return entity_id, description, link
    else:
        return entity_id, '在HTML文本中未找到Description。', None

# 假设txt文件名为"html_text.txt"
file_path = "C:/Users/jky/Desktop/request_text.txt"

# 读取txt文件，并处理每个HTML文本段
with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

# 定义HTML文本段的分隔符
separator = '<tr class="tc-row visi-parent "'

# 使用分隔符将文本分成不同的HTML文本段
html_texts = file_content.split(separator)[1:]

# 处理每个HTML文本段
for html_text in html_texts:
    # 添加回分隔符到每个段的开头
    html_text = separator + html_text
    entity_id, description, link = process_html_text(html_text)
    print('ID:', entity_id, 'Description:', description, 'Link:', link)
    count += 1

print(count)

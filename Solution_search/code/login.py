from bs4 import BeautifulSoup
import requests
import urllib3.exceptions

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 登录页面的URL和登录信息
login_url = 'https://10.60.1.66'
username = 'giles.zhou'
password = 'Tobizit@2023'

# 创建一个会话对象
session = requests.Session()

# 发送登录请求
login_data = {
    'j_username': username,
    'j_password': password,
    'loginButton': 'Log in'
}
response = session.post(login_url, data=login_data, verify=False)

# 检查登录是否成功
if response.ok:
    print('Login successful')

    # 在会话中继续进行其他请求，保持登录状态
    # 获取需要登录才能访问的页面的内容
    protected_page_url = 'https://10.60.1.66/HomePage.do?view_type=my_view'
    protected_page_response = session.get(protected_page_url)

    # 检查受保护页面获取是否成功
    if protected_page_response.ok:
        print('Protected page content:')
        print(protected_page_response.text)

        # 使用 Beautiful Soup 解析 HTML 内容
        soup = BeautifulSoup(protected_page_response.text, 'html.parser')

        # 找到所有符合要求的信息
        target_elements = soup.find_all('td', class_='evenRow')  # 根据您的需求调整选择器

        # 遍历并输出每个信息的内容
        for element in target_elements:
            link = element.find('a')
            if link:
                link_text = link.get_text()
                link_url = link['href']
                print(f"链接文字：{link_text}")
                print(f"链接地址：{link_url}")
                print("-" * 20)
    else:
        print('Failed to retrieve protected page content')

else:
    print('Login failed')

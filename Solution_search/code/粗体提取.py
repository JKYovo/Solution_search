# function: 从HTML文本中提取粗体文本
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
count = 0
file_path = "C:/Users/jky/Desktop/request_text.txt"

# 读取txt文件，并处理每个HTML文本段
with open(file_path, 'r', encoding='utf-8') as file:
    html_text = file.read()

# html_text = '''
# <tr class="tc-row visi-parent unread-item" data-cs-field="row" data-entityid="3314"><td style="width:31px" class="headercheckbox headercheckbox "><div class="d_w " style="width:31px"><input type="checkbox" name="checkbox" value="3314" templateid="1501" data-table-checkbox="" aria-label="Request List"></div></td><td style="width:90px" class=""><div class="d_w " style="width:90px" rel="uitooltip-track-table" title="3314">3314</div></td><td style="width:150px" class=""><div class="d_w " style="width:150px"><span class="disp-ib p3 truncate-ellipsis "><span class="truncate-wrapper"><a style="background-color:transparent" class="sb" data-spa="true" data-spa-page="request-details" data-spa-module="requests" href="WorkOrder.do?woMode=viewWO&amp;woID=3314&amp;fromListView=true" "="" rel="uitooltip-track" title="<strong>Request ID :</strong>3314<br><strong>Category :</strong> - <br><strong>Subject :</strong> CUCM Q931 debug <br><strong>Description :</strong>  <br> ">CUCM Q931 debug</a></span></span></div></td></tr>
# <tr class="tc-row visi-parent unread-item" data-cs-field="row" data-entityid="3211"><td style="width:31px" class="headercheckbox headercheckbox "><div class="d_w " style="width:31px"><input type="checkbox" name="checkbox" value="3211" templateid="945" data-table-checkbox="" aria-label="Request List"></div></td><td style="width:90px" class=""><div class="d_w " style="width:90px" rel="uitooltip-track-table" title="3211">3211</div></td><td style="width:150px" class=""><div class="d_w " style="width:150px"><span class="disp-ib p3 truncate-ellipsis "><span class="truncate-wrapper"><a style="background-color:transparent" class="sb" data-spa="true" data-spa-page="request-details" data-spa-module="requests" href="WorkOrder.do?woMode=viewWO&amp;woID=3211&amp;fromListView=true" "="" rel="uitooltip-track" title="<strong>Request ID :</strong>3211<br><strong>Category :</strong> - <br><strong>Subject :</strong> AD&amp;#x670d;&amp;#x52a1;&amp;#x5668;GPO&amp;#x8c03;&amp;#x6574; <br><strong>Description :</strong> Alan:你看你啥时候有空，一起看下怎么弄好哇D4C:明早可以吗Alan:周五你看行吗？我明后天可能不在公司D4C:行 <br> ">AD服务器GPO调整</a></span></span></div></td></tr>
# <tr class="tc-row visi-parent unread-item" data-cs-field="row" data-entityid="3195"><td style="width:31px" class="headercheckbox headercheckbox "><div class="d_w " style="width:31px"><input type="checkbox" name="checkbox" value="3195" templateid="361" data-table-checkbox="" aria-label="Request List"></div></td><td style="width:90px" class=""><div class="d_w " style="width:90px" rel="uitooltip-track-table" title="3195">3195</div></td><td style="width:150px" class=""><div class="d_w " style="width:150px"><span class="disp-ib p3 truncate-ellipsis "><span class="truncate-wrapper"><a style="background-color:transparent" class="sb" data-spa="true" data-spa-page="request-details" data-spa-module="requests" href="WorkOrder.do?woMode=viewWO&amp;woID=3195&amp;fromListView=true" "="" rel="uitooltip-track" title="<strong>Request ID :</strong>3195<br><strong>Category :</strong> - <br><strong>Subject :</strong> &amp;#x7814;&amp;#x7cbe;&amp;#x820d;&amp;#x5b63;&amp;#x5ea6;&amp;#x5de1;&amp;#x68c0; <br><strong>Description :</strong>  <br> ">研精舍季度巡检</a></span></span></div></td></tr>
# '''

soup = BeautifulSoup(html_text, 'html.parser')

# 找到所有包含请求信息的 <tr> 元素
request_rows = soup.find_all('tr', class_='tc-row')

# 用于存储提取的数据
data = []

# 遍历每个 <tr> 元素，提取信息
for row in request_rows:
    entity_id = row['data-entityid']

    a_tag = row.find('a', {'data-spa-module': 'requests', 'class': 'sb'})
    if a_tag:
        description_title = a_tag['title']
        description_soup = BeautifulSoup(description_title, 'html.parser')
        description_strong = description_soup.find('strong', string='Description :')
        if description_strong:
            description = description_strong.next_sibling.strip()
            description_text = ''
            for sibling in description_strong.next_siblings:
                if sibling.name == 'br':
                    break
                if sibling.name == 'a':
                    description_text += sibling.get_text(strip=True)
                else:
                    description_text += str(sibling)
            description = description_text.strip()
        else:
            description = 'Description 未找到'
        link = a_tag['href']
    else:
        description = '在 HTML 文本中未找到 Description。'
        link = None

    data.append({
        'ID': entity_id,
        'Description': description,
        'Link': link
    })


# 输出提取的数据
for item in data:
    if item['Link'] is not None:
        print('ID:', item['ID'], 'Description:', item['Description'], 'Link:', item['Link'])
        count += 1
print('共提取', count, '条数据。')
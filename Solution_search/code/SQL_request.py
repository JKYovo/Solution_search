import pandas as pd
import MySQLdb

# 读取Excel文件到Pandas DataFrame
file_path = 'C:/Users/jky/Desktop/request.xlsx'
df = pd.read_excel(file_path, header=None, names=['ID', '主题', '创建日', '逾期时间', '请求人', '技术员', '账户', '地点', '描述', '链接'])

# 处理 NaN 值，将其替换为空字符串
df = df.fillna('')

# 连接到MySQL数据库
db_username = 'root'
db_password = 'jikeyv2003.'
db_host = '127.0.0.1'
db_port = '3306'
db_name = 'solve'

db = MySQLdb.connect(host=db_host, port=int(db_port), user=db_username, passwd=db_password, db=db_name)

# 创建数据库游标
cursor = db.cursor()

# 创建表
table_name = 'request'
create_table_query = f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        主题 VARCHAR(255),
        创建日 VARCHAR(30),
        逾期时间 VARCHAR(30),
        请求人 VARCHAR(255),
        技术员 VARCHAR(255),
        账户 VARCHAR(255),
        地点 VARCHAR(255),
        描述 TEXT,
        链接 VARCHAR(255)
    )
'''
cursor.execute(create_table_query)

# 将DataFrame数据插入MySQL数据库
for _, row in df.iterrows():
    insert_query = f'''
        INSERT INTO {table_name} (ID, 主题, 创建日, 逾期时间, 请求人, 技术员, 账户, 地点, 描述, 链接)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    data = (row['ID'], row['主题'], row['创建日'], row['逾期时间'], row['请求人'], row['技术员'], row['账户'], row['地点'], row['描述'], row['链接'])
    cursor.execute(insert_query, data)

# 提交事务并关闭连接
db.commit()
db.close()

print("数据已成功存入MySQL数据库中。")

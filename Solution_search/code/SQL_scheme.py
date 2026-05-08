import pandas as pd
import MySQLdb
import os
import sys

# 读取Excel文件到Pandas DataFrame
file_path = sys.argv[1] if len(sys.argv) > 1 else 'data/new_data.xlsx'
df = pd.read_excel(file_path, header=None, names=['ID', '标题', '主题', '描述', '创建人', '链接'])

# 处理 NaN 值，将其替换为空字符串
df = df.fillna('')

# 连接到MySQL数据库
db_username = os.environ.get('DB_USER', 'root')
db_password = os.environ.get('DB_PASSWORD', '')
db_host = os.environ.get('DB_HOST', '127.0.0.1')
db_port = os.environ.get('DB_PORT', '3306')
db_name = os.environ.get('DB_NAME', 'solve')

db = MySQLdb.connect(host=db_host, port=int(db_port), user=db_username, passwd=db_password, db=db_name)

# 创建数据库游标
cursor = db.cursor()

# 创建表
table_name = 'scheme'
create_table_query = f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        标题 VARCHAR(255),
        主题 VARCHAR(255),
        描述 TEXT,
        创建人 VARCHAR(255),
        链接 VARCHAR(255)
    )
'''
cursor.execute(create_table_query)

# 将DataFrame数据插入MySQL数据库
for _, row in df.iterrows():
    insert_query = f'''
        INSERT INTO {table_name} (ID, 标题, 主题, 描述, 创建人, 链接)
        VALUES (%s, %s, %s, %s, %s, %s)
    '''
    data = (row['ID'], row['标题'], row['主题'], row['描述'], row['创建人'], row['链接'])
    cursor.execute(insert_query, data)

# 提交事务并关闭连接
db.commit()
db.close()

print("数据已成功存入MySQL数据库中。")

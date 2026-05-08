# Solution_search

解决方案 / 请求检索工具。项目基于 Django 构建，用来整理运维请求、解决方案条目，并提供列表检索、条件筛选、增删改查和外部搜索入口。

## 功能概览

- 解决方案列表：支持标题、主题、描述、创建人等字段检索。
- 请求列表：支持主题、日期、技术员、账户、描述等字段检索。
- 数据维护：支持新增、编辑、删除解决方案和请求记录。
- 数据处理脚本：`Solution_search/code/` 下保留了 Excel、HTML、文本解析和 MySQL 导入脚本，便于从历史数据中整理内容。
- 搜索入口：保留百度、Bing、Google 跳转入口。

## 技术栈

- Python 3.9+
- Django 4.2
- MySQL
- Bootstrap 3
- pandas / openpyxl / BeautifulSoup

## 本地运行

```bash
cd Solution_search
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

按本机 MySQL 配置修改 `.env` 后运行：

```bash
cd Solution_search
python manage.py check
python manage.py runserver
```

浏览器访问 `http://127.0.0.1:8000/`。

## 配置说明

项目通过环境变量读取 Django 和数据库配置，避免在代码中保存本机密码。

| 变量 | 说明 | 默认值 |
| --- | --- | --- |
| `DJANGO_SECRET_KEY` | Django 密钥 | `change-me-in-local-dev` |
| `DJANGO_DEBUG` | 是否开启调试模式 | `true` |
| `DJANGO_ALLOWED_HOSTS` | 允许访问的 Host，逗号分隔 | `*` |
| `DB_ENGINE` | Django 数据库引擎 | `django.db.backends.mysql` |
| `DB_NAME` | 数据库名 | `solve` |
| `DB_USER` | 数据库用户名 | `root` |
| `DB_PASSWORD` | 数据库密码 | 空 |
| `DB_HOST` | 数据库地址 | `127.0.0.1` |
| `DB_PORT` | 数据库端口 | `3306` |

## 数据处理脚本

`Solution_search/code/` 中的脚本是历史数据清洗工具，建议通过命令行参数指定输入输出路径，例如：

```bash
python code/excel_process.py data/source.xlsx data/new_data.xlsx
python code/get_link.py data/html.txt data/links.txt
python code/SQL_scheme.py data/new_data.xlsx
```

数据库导入脚本会复用 `DB_HOST`、`DB_PORT`、`DB_USER`、`DB_PASSWORD`、`DB_NAME` 环境变量。

## 历史说明

这是早期用于练习 Django 并解决实际检索需求的项目。当前整理重点是保留可读的项目结构、运行说明和配置方式，未进行大规模业务重构。

# 遍历了 page_range 中的每个页码 i，然后对每个页码都调用了一个名为 generate_page_element 的函数
from django.utils.safestring import mark_safe


class Pagination(object):
    def __init__(self, current_page, total_count, base_url, per_page_count=10, max_pager_count=11):
        """
        :param current_page: 当前页
        :param total_count:  数据库中总条数
        :param base_url:  基础URL
        :param per_page_count: 每页显示的数据条数
        :param max_pager_count: 最多显示的页码个数
        """
        self.base_url = base_url
        self.current_page = current_page
        self.total_count = total_count
        self.per_page_count = per_page_count
        self.max_pager_count = max_pager_count

    @property
    def total_page_count(self):
        # 总页数
        v, a = divmod(self.total_count, self.per_page_count)
        if a:
            v += 1
        return v

    def page_str(self):
        # 生成页码的HTML
        page_list = []

        # 如果总页数 < 最多显示的页码个数
        if self.total_page_count < self.max_pager_count:
            # 则最多显示的页码个数 = 总页数
            self.max_pager_count = self.total_page_count
        else:
            # 否则，最多显示的页码个数 = 最多显示的页码个数
            self.max_pager_count = self.max_pager_count

        # 如果总页数 < 最多显示的页码个数
        if self.total_page_count < self.max_pager_count:
            # 则最多显示的页码个数 = 总页数
            max_pager_count = self.total_page_count
        else:
            # 否则，最多显示的页码个数 = 最多显示的页码个数
            max_pager_count = self.max_pager_count

        # 如果当前页 <= 最多显示的页码个数的一半
        if self.current_page <= max_pager_count // 2:
            # 则起始页码 = 1
            start = 1
            # 结束页码 = 最多显示的页码个数
            end = max_pager_count
        else:
            # 否则，起始页码 = 当前页 - 最多显示的页码个数的一半
            start = self.current_page - max_pager_count // 2
            # 结束页码 = 当前页 + 最多显示的页码个数的一半
            end = self.current_page + max_pager_count // 2

            # 如果当前页 + 最多显示的页码个数的一半 > 总页数
            if end > self.total_page_count:
                # 则起始页码 = 总页数 - 最多显示的页码个数 + 1
                start = self.total_page_count - max_pager_count + 1
                # 结束页码 = 总页数
                end = self.total_page_count

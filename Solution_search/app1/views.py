# solutions/views.py

import requests
from django import forms
from django.shortcuts import render, redirect
from .models import Scheme, Request
from app1 import models
from django.db.models import Q
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.http import HttpResponse



# from utils.pagination import Pagination


def generate_page_element(page_number, current_page, url_params):
    if page_number == current_page:
        return '<li class="active"><a href="?{}&page={}">{}</a></li>'.format(url_params, page_number, page_number)
    else:
        return '<li><a href="?{}&page={}">{}</a></li>'.format(url_params, page_number, page_number)


# 遍历了 page_range 中的每个页码 i，然后对每个页码都调用了一个名为 generate_page_element 的函数
def generate_pagination(total_pages, current_page, page_range, url_params):
    page_list = []

    if current_page > 1:
        prev_page = current_page - 1
        prev_url = "?" + url_params + "page=" + str(prev_page)
        prev_element = '<li><a href="{}">上一页</a></li>'.format(prev_url)
        page_list.append(prev_element)

    if current_page > 3:
        first_url = "?" + url_params + "page=1"
        first_element = '<li><a href="{}">首页</a></li>'.format(first_url)
        page_list.append(first_element)

    for i in page_range:
        page_element = generate_page_element(i, current_page, url_params)
        page_list.append(page_element)

    if current_page < total_pages - 2:
        last_url = "?" + url_params + "page=" + str(total_pages)
        last_element = '<li><a href="{}">尾页</a></li>'.format(last_url)
        page_list.append(last_element)

    if current_page < total_pages:
        next_page = current_page + 1
        next_url = "?" + url_params + "page=" + str(next_page)
        next_element = '<li><a href="{}">下一页</a></li>'.format(next_url)
        page_list.append(next_element)

    return mark_safe("".join(page_list))


def scheme_list(request):
    # page_obj = Pagination(request.GET.get('page', '1'), models.Scheme.objects.all().count(), request.GET.copy(), 10)
    page = request.GET.get('page', "1")
    page_size = 10
    start = (int(page) - 1) * page_size
    end = int(page) * page_size

    search_data = request.GET.get('q', "")
    biaoti_data = request.GET.get('biao_ti', "")
    zhuti_data = request.GET.get('zhu_ti', "")
    miaoshu_data = request.GET.get('miao_shu', "")

    queryset = models.Scheme.objects.all().order_by('-ID')

    url_params = ""

    if search_data:
        # 构建一个空的 Q 对象
        combined_query = Q()

        # 需要搜索的列名列表
        columns_to_search = ['ID', '标题', '主题', '描述', '创建人']

        # 将多个列名的 Q 对象合并到一个 Q 对象中
        for column in columns_to_search:
            combined_query |= Q(**{f"{column}__icontains": search_data})

        # 执行查询
        queryset = queryset.filter(combined_query)

        # 构建 URL 参数
        url_params += "q=" + search_data + "&"

    if biaoti_data:
        queryset = queryset.filter(Q(标题__icontains=biaoti_data))
        url_params += "biao_ti=" + biaoti_data + "&"
    if zhuti_data:
        queryset = queryset.filter(Q(主题__icontains=zhuti_data))
        url_params += "zhu_ti=" + zhuti_data + "&"
    if miaoshu_data:
        queryset = queryset.filter(Q(描述__icontains=miaoshu_data))
        url_params += "miao_shu=" + miaoshu_data + "&"

    total_count = queryset.count()
    total_page_count, div = divmod(total_count, page_size)
    if div:
        total_page_count += 1

    plus = 5
    start_page = max(int(page) - plus, 1)
    end_page = min(int(page) + plus + 1, total_page_count + 1)
    page_range = range(start_page, end_page)
    page_string = generate_pagination(total_page_count, int(page), page_range, url_params)

    queryset = queryset[start:end]

    return render(request, 'scheme_list.html', {
        'queryset': queryset,
        'search_data': search_data,
        'biaoti_data': biaoti_data,
        'zhuti_data': zhuti_data,
        'miaoshu_data': miaoshu_data,
        'page_string': page_string,
    })


def request_list(request):
    # page_obj = Pagination(request.GET.get('page', '1'), models.Request.objects.all().count(), request.GET.copy(), 10)
    page = request.GET.get('page', "1")
    page_size = 10
    start = (int(page) - 1) * page_size
    end = int(page) * page_size

    search_data = request.GET.get('q', "")
    zhuti_data = request.GET.get('zhu_ti', "")
    riqi_data = request.GET.get('ri_qi', "")
    jishuyuan_data = request.GET.get('ji_shu_yuan', "")
    zhanghu_data = request.GET.get('zhang_hu', "")
    miaoshu_data = request.GET.get('miao_shu', "")

    queryset = models.Request.objects.all().order_by('-ID')

    url_params = ""

    if search_data:
        # 构建一个空的 Q 对象
        combined_query = Q()

        # 需要搜索的列名列表
        columns_to_search = ['ID', '主题', '创建日', '逾期时间', '请求人', '技术员', '账户', '地点', '描述']

        # 将多个列名的 Q 对象合并到一个 Q 对象中
        for column in columns_to_search:
            combined_query |= Q(**{f"{column}__icontains": search_data})

        # 执行查询
        queryset = queryset.filter(combined_query)

        # 构建 URL 参数
        url_params += "q=" + search_data + "&"

    if zhuti_data:
        queryset = queryset.filter(Q(主题__icontains=zhuti_data))
        url_params += "zhu_ti=" + zhuti_data + "&"
    if riqi_data:
        queryset = queryset.filter(Q(创建日__icontains=riqi_data) | Q(逾期时间__icontains=riqi_data))
        url_params += "ri_qi=" + riqi_data + "&"
    if jishuyuan_data:
        queryset = queryset.filter(Q(技术员__icontains=jishuyuan_data))
        url_params += "ji_shu_yuan=" + jishuyuan_data + "&"
    if zhanghu_data:
        queryset = queryset.filter(Q(账户__icontains=zhanghu_data))
        url_params += "zhang_hu=" + zhanghu_data + "&"
    if miaoshu_data:
        queryset = queryset.filter(Q(描述__icontains=miaoshu_data))
        url_params += "miao_shu=" + miaoshu_data + "&"

    total_count = queryset.count()
    total_page_count, div = divmod(total_count, page_size)
    if div:
        total_page_count += 1

    plus = 5
    start_page = max(int(page) - plus, 1)
    end_page = min(int(page) + plus + 1, total_page_count + 1)
    page_range = range(start_page, end_page)
    page_string = generate_pagination(total_page_count, int(page), page_range, url_params)

    queryset = queryset[start:end]

    return render(request, 'request_list.html', {
        'queryset': queryset,
        'search_data': search_data,
        'zhuti_data': zhuti_data,
        'riqi_data': riqi_data,
        'jishuyuan_data': jishuyuan_data,
        'zhanghu_data': zhanghu_data,
        'miaoshu_data': miaoshu_data,
        'page_string': page_string,
    })


class SchemeModelForm(forms.ModelForm):
    class Meta:
        model = Scheme  # 指定模型,这是数据库名称
        fields = "__all__"  # 指定显示的字段

    def __init__(self, *args, **kwargs):
        super(SchemeModelForm, self).__init__(*args, **kwargs)
        self.fields['ID'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': '必填', 'autofocus': 'autofocus'})
        self.fields['标题'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': '必填'})
        self.fields['主题'].widget.attrs.update({'class': 'form-control', 'placeholder': '选填'})
        self.fields['描述'].widget.attrs.update({'class': 'form-control', 'placeholder': '选填'})
        self.fields['创建人'].widget.attrs.update({'class': 'form-control', 'placeholder': '选填'})
        self.fields['链接'].widget.attrs.update({'class': 'form-control', 'placeholder': '必填(复制该方案的链接)'})


class RequestModelForm(forms.ModelForm):
    class Meta:
        model = Request  # 指定模型,这是数据库名称
        fields = "__all__"  # 指定显示的字段

    def __init__(self, *args, **kwargs):
        super(RequestModelForm, self).__init__(*args, **kwargs)
        self.fields['ID'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': '必填', 'autofocus': 'autofocus'})
        self.fields['主题'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': '必填'})
        self.fields['创建日'].widget.attrs.update({'class': 'form-control', 'placeholder': '选填'})
        self.fields['逾期时间'].widget.attrs.update({'class': 'form-control', 'placeholder': '选填'})
        self.fields['请求人'].widget.attrs.update({'class': 'form-control', 'placeholder': '选填'})
        self.fields['技术员'].widget.attrs.update({'class': 'form-control', 'placeholder': '选填'})
        self.fields['账户'].widget.attrs.update({'class': 'form-control', 'placeholder': '选填'})
        self.fields['地点'].widget.attrs.update({'class': 'form-control', 'placeholder': '选填'})
        self.fields['描述'].widget.attrs.update({'class': 'form-control', 'placeholder': '选填'})
        self.fields['链接'].widget.attrs.update({'class': 'form-control', 'placeholder': '必填(复制该方案的链接)'})


def scheme_edit(request, nid):
    """ 编辑 """
    row_object = models.Scheme.objects.filter(ID=nid).first()

    if request.method == "GET":
        form = SchemeModelForm(instance=row_object)
        return render(request, 'scheme_edit.html', {"form": form})

    form = SchemeModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/scheme/list')

    return render(request, 'scheme_edit.html', {"form": form})


def request_edit(request, nid):
    """ 编辑 """
    row_object = models.Request.objects.filter(ID=nid).first()

    if request.method == "GET":
        form = RequestModelForm(instance=row_object)
        return render(request, 'request_edit.html', {"form": form})

    form = RequestModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/request/list')

    return render(request, 'request_edit.html', {"form": form})


def scheme_add(request):
    if request.method == "GET":
        form = SchemeModelForm()
        return render(request, 'scheme_add.html', {"form": form})
    form = SchemeModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/scheme/list')
    return render(request, 'scheme_add.html', {"form": form})


def request_add(request):
    if request.method == "GET":
        form = RequestModelForm()
        return render(request, 'request_add.html', {"form": form})
    form = RequestModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/request/list')
    return render(request, 'request_add.html', {"form": form})


def request_delete(request, nid):
    models.Request.objects.filter(ID=nid).delete()
    return redirect('/request/list')


def help(request):
    return render(request, 'help.html')


def search(request):
    template_path = 'index.html'  # 指定正确的模板路径
    html_content = render_to_string(template_path)
    return HttpResponse(html_content)


def search_solution(request):
    keyword = request.GET.get('keyword', '')
    solutions = Scheme.objects.filter(标题__icontains=keyword)
    return render(request, 'search_results.html')


def search_request(request):
    keyword = request.GET.get('keyword', '')
    requests = Request.objects.filter(主题__icontains=keyword)
    return render(request, 'search_results.html')


def baidu(request):
    if 'q' in request.GET:
        keyword = request.GET['q']
        # 调用百度搜索API，并获取搜索结果
        url = f'https://www.baidu.com/s?wd={keyword}'
        return redirect(url)
    else:
        return render(request, 'baidu.html')


def bing(request):
    return redirect('https://www.bing.com/')


def google(request):
    return redirect('https://www.google.com.hk/')


def scheme_delete(request, nid):
    # 删除前先确认
    models.Scheme.objects.filter(ID=nid).delete()
    return redirect('/scheme/list')

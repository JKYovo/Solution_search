# solutions/models.py
from django.db import models


class Scheme(models.Model):
    ID = models.IntegerField(primary_key=True, unique=True)
    标题 = models.CharField(max_length=255, null=False, blank=False)
    主题 = models.CharField(max_length=255, null=True, blank=True)
    描述 = models.TextField(null=True, blank=True)
    创建人 = models.CharField(max_length=255, null=False, blank=True)
    链接 = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.标题  # 或者使用其他适当的字段

    class Meta:
        db_table = 'scheme'  # 表名


class Request(models.Model):
    ID = models.IntegerField(primary_key=True, unique=True)
    主题 = models.CharField(max_length=255, null=False, blank=False)
    创建日 = models.CharField(max_length=30, null=False, blank=True)
    逾期时间 = models.CharField(max_length=30, null=False, blank=True)
    请求人 = models.CharField(max_length=255, null=False, blank=True)
    技术员 = models.CharField(max_length=255, null=False, blank=True)
    账户 = models.CharField(max_length=255, null=False, blank=True)
    地点 = models.CharField(max_length=255, null=False, blank=True)
    描述 = models.TextField(null=True, blank=True)
    链接 = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.主题  # 或者使用其他适当的字段

    class Meta:
        db_table = 'request'  # 表名
# 如果有外键关系，也需要相应地进行调整
# class OtherModel(models.Model):
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     ...

# 如果需要其他的模型，继续在这里添加

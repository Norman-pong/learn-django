from django.db import models
from datetime import date


# Create your models here.
import django.utils.timezone as timezone
class Department(models.Model):
    today = date.today()
    title = models.CharField(verbose_name='标题', max_length=20)
    add_date = models.DateTimeField(verbose_name='创建时间', default=timezone.now, db_comment='部门创建时间')
    mod_date = models.DateTimeField(verbose_name='创建时间', auto_now=True, db_comment='部门修改时间')

    def __str__(self) -> str:
        return self.title


class Employee(models.Model):
    name = models.CharField(verbose_name='员工名称', max_length=20)
    age = models.IntegerField(verbose_name='员工年龄')
    account = models.CharField(verbose_name='员工账号', max_length=20)
    password = models.CharField(verbose_name='员工密码', max_length=20)
    hiredate = models.DateTimeField(verbose_name='入职时间')

    # 联表加约束条件
    '''
    联表约束
        1. 关联部门的在插入数据时检验是否存在
        2. 当部门表删除数据时，员工表有所关联的数据将“联级删除”
    '''
    # depart = models.ForeignKey(to=Department, to_field=)
    depart = models.ForeignKey(verbose_name='部门' ,to=Department, to_field='id', on_delete=models.CASCADE)
    # 置空处理
    # depart = models.ForeignKey(to='Department', to_field='id', null=True, blank=True, on_delete=models.SET_NULL)

    # 性别约束
    gender_choices = (
        (1,'男'),
        (2,'女')
    )
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)


class PrettyNum(models.Model):
    mobile = models.CharField(verbose_name='手机号码', max_length=11)
    price = models.IntegerField(verbose_name='价格', default=0)

    level_choices = (
        (1, '一级'),
        (2, '二级'),
        (3, '三级'),
        (4, '四级'),
        (5, '五级'),
    )

    level = models.SmallIntegerField(verbose_name='手机等级', choices=level_choices, default=1)

    status_choices = (
        (1, '未启用'),
        (2, '已使用')
    )
    status = models.SmallIntegerField(verbose_name='手机号使用状态', choices=status_choices, default=1)
    create_date = models.DateTimeField(verbose_name='创建时间', auto_created=True, default=date.today())
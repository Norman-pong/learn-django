import json
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse, QueryDict
from django.forms import ModelForm
from django import forms
from django.views import View
from app02.models import Department, Employee, PrettyNum


# Create your views here.
def dept_index(request):
    dept_list = Department.objects.all()
    print(dept_list)
    return render(request, 'list.html', {"dept_list": dept_list})


def employee_index(request):
    list = Employee.objects.all()
    context = {
        'depart_list': Department.objects.all(),
        'gender_choices': Employee.gender_choices
    }
    # for obj in list:
    #     print('转换数据库数据 --> ', obj.get_gender_display(), obj.hiredate.strftime('%Y-%m-%d'))
    #     print('联表查询部门表 --> ', obj.depart.title)
    return render(request, 'employees.html', {'employees': list, 'context' :context})


class EmployeeForm(ModelForm):
    # 需要独立编写校验规则
    name = forms.CharField(min_length=2,label='员工姓名')
    password = forms.CharField(min_length=6,label='员工密码')
    hiredate_attrs = {'placeholder': "yyyy-MM-dd",'class': 'layui-input','lay-verify':'date','id':'date','autocomplete':'off'}
    hiredate = forms.DateTimeField(label='入职时间',widget=forms.TextInput(attrs=hiredate_attrs))
    class Meta:
        model = Employee
        fields = ['name', 'password', 'gender', 'age', 'account', 'hiredate','depart']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
          # 通过插件添加 input 属性
          if name == 'hiredate':
              continue
          field.widget.attrs = {"class": 'layui-input', "lay-verify": "required", "placeholder": "请输入{}".format(field.label),'autocomplete':'off'}


def employee_add_user_form(request):
    if request.method == 'GET':
      form = EmployeeForm()
      return render(request, 'employees_add.html', { 'form': form})
    if request.method == 'POST':
        form = EmployeeForm(data=request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'employees_add.html', { 'form': form})
    return redirect('/employee/list')


def employee_add_user(request):
    if(request.method == 'POST'):
      data = json.loads(request.body)
      Employee.objects.create(**data)
    res_data = {"code": 200, "data": data, "msg": "保存成功"}
    return JsonResponse(res_data)


def employee_edit_user(request, nid):
    row_object = Employee.objects.filter(id=nid).first()
    if request.method == 'GET':
      form = EmployeeForm(instance=row_object)
      return render(request,'employees_edit.html', { 'form':form})

    form = EmployeeForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return render(request, 'employees_edit.html', { 'form': form})
    else:
        return render(request, 'employees_edit.html', { 'form': form})


def dept(request):
    nid = request.params.get('id')
    dept_name = request.params.get('deptName')

    if request.method == 'POST':
        Department.objects.create(title=dept_name)

    if request.method == 'PUT':
        Department.objects.filter(id=nid).update(title=dept_name)

    if request.method == 'DELETE':
        Department.objects.filter(id=nid).delete()

    res_data = {"code": 200, "data": dept_name, "msg": "请求成功"}
    return JsonResponse(res_data)


class PrettyNumForm(ModelForm):
    # 需要独立编写校验规则
    mobile = forms.IntegerField(min_value=11,label='手机号码')
    # password = forms.CharField(min_length=6,label='员工密码')
    # hiredate_attrs = {'placeholder': "yyyy-MM-dd",'class': 'layui-input','lay-verify':'date','id':'date','autocomplete':'off'}
    # hiredate = forms.DateTimeField(label='入职时间',widget=forms.TextInput(attrs=hiredate_attrs))
    class Meta:
        model = PrettyNum
        fields = ['mobile', 'price', 'level','status',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
          # # 通过插件添加 input 属性
          # if name == 'hiredate':
          #     continue
          field.widget.attrs = {"class": 'layui-input', "lay-verify": "required", "placeholder": "请输入{}".format(field.label),'autocomplete':'off'}

class Mobile(View):
    def get(self, request):
        list = PrettyNum.objects.all()
        form = PrettyNumForm()
        return render(request, 'mobile/list.html', { 'mobile_list' : list, 'form': form})

    def post(self, request):
        data = json.loads(request.body)
        PrettyNum.objects.create(**data)
        return HttpResponse(request)

    def delete(self, request):
        return HttpResponse(request)

import json
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, QueryDict
from app02.models import Department, Employee


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
    for obj in list:
        print('转换数据库数据 --> ', obj.get_gender_display(), obj.hiredate.strftime('%Y-%m-%d'))
        print('联表查询部门表 --> ', obj.depart.title)
    return render(request, 'employees.html', {'employees': list, 'context' :context})


def employee_add_user(request):
    if(request.method == 'POST'):
      data = json.loads(request.body)
      Employee.objects.create(**data)
    res_data = {"code": 200, "data": data, "msg": "保存成功"}
    return JsonResponse(res_data)


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

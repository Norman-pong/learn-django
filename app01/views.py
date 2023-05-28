from django.shortcuts import render, HttpResponse, redirect
from app01.models import UserList

# Create your views here.


def index(request):
    return HttpResponse('主页')


def home_index(request):
    return render(request, "home_index.html")


def home_templates(request):
    return render(request, "home_templates.html")


def grammar_summary(request):
    name = '测试名字'
    arr = ['数据1', '数据2', '数据3']
    obj = {
        'name': '测试名字2',
        'age': 18,
        'info': {
            'parent_name': '爸爸',
            'parent_age': 49
        }
    }
    arr_obj = [{'age': 19, 'name': '测试名字3'}, obj, obj, obj]

    import requests

    res = requests.get(
        'https://jsonplaceholder.typicode.com/todos/2')
    
    vendor_data_list = res.json()

    return render(request,
                  'grammar/summary.html',
                  {'name': name,
                   'arr': arr,
                   'obj': obj,
                   'arr_obj': arr_obj,
                   'vender_data_list': vendor_data_list
                   })


def user_login(request):
    if request.method == 'GET':
        return render(request, "user/login.html")
    post_data = request.POST
    username = post_data.get('username')
    password = post_data.get('password')
    if username == 'admin':
        return redirect('/grammar/summary')

    return render(request, "user/login.html", {"errMsg": "密码错误"})


def user_list(request):
    data_list = UserList.objects.all()
    print(data_list)
    return render(request, "user/list.html", {'data_list': data_list})


def user_add(request):
    if request.method == 'GET':
        return render(request, "user/add.html")

    post_data = request.POST
    username = post_data.get('username')
    password = post_data.get('password')
    remark = post_data.get('remark')
    age = post_data.get('age') or 0
    UserList.objects.create(
        username=username, password=password, age=age, remark=remark)
    return redirect('/user/list')


def user_delete(request):
    id = request.GET.get('id')
    print(id)
    if id:
        UserList.objects.filter(id=id).delete()
        return redirect('/user/list')

    return HttpResponse('id 不能为空')
from django.shortcuts import render, HttpResponse

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
    print('---------')
    vender_data_list = res.json()
    print(vender_data_list)

    return render(request,
                  'grammar/summary.html',
                  {'name': name,
                   'arr': arr,
                   'obj': obj,
                   'arr_obj': arr_obj,
                   'vender_data_list': vender_data_list
                   })

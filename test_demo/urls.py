from app01 import views
from app02 import views as app02_views
from app02.models import Department, Employee, PrettyNum
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['url', 'name', 'age', 'account',
                  'password', 'hiredate', 'gender', 'depart']


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['url', 'title', 'add_date', 'mod_date']


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class PrettyNumSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrettyNum
        fields = ['url', 'mobile', 'price', 'level', 'status']


class PrettyNumViewSet(viewsets.ModelViewSet):
    queryset = PrettyNum.objects.all()
    serializer_class = PrettyNumSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'employee', EmployeeViewSet)
router.register(r'department', DepartmentViewSet)
router.register(r'pretty_num', PrettyNumViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    # DRF
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),


    # path('', RedirectView.as_view(url='employee/list')),
    path('home/', views.home_index),
    path('home/templates', views.home_templates),
    path('grammar/summary', views.grammar_summary),

    # 登录案例
    path('user/add', views.user_add),
    path('user/list', views.user_list),
    path('user/login', views.user_login),
    path('user/delete', views.user_delete),


    # FBV 模式
    path('dept/list', app02_views.dept_index),
    path('employee/list', app02_views.employee_index),
    path('employee/add', app02_views.employee_add_user_form),
    path('employee/<int:nid>/edit', app02_views.employee_edit_user),
    path('employee/<int:nid>/delete', app02_views.employee_delete_user),


    # CBV 模式 - mobile
    path('mobile/list', app02_views.Mobile.as_view()),
    path('mobile/<int:nid>', app02_views.mobile_list),
    # path('mobile/<int:nid>', app02_views.mobile_form_prompt),

    # API
    path('api/dept', app02_views.dept),
    path('api/employee/add_user', app02_views.employee_add_user)
]

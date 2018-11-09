from django.urls import path
from . import views
urlpatterns = [
    path('', views.show, name='show'),
    path('<int:id>/', views.content, name='content'),
    path('?q', views.search, name='search'),
    path('addstudent/', views.addstudent, name='addstudent'),
    path('?name', views.adddstu, name='addstu'),
    path('addcourse/', views.course, name='course'),
    path('?course', views.addcourse, name='addcourse'),
    path('students/', views.students, name='students'),
    path('students/delete/<int:id>/', views.deleteStudent, name='delete'),
]

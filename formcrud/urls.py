from django.urls import path
from formcrud import views

## url paths
urlpatterns = [
    path("",views.index,name="index"),
    path("show/",views.index,name="show"),
    path("register/",views.formApi,name="register")
]
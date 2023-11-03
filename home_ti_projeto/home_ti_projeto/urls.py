
from django.contrib import admin
from django.urls import path
from app_home_ti_full import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ti_full/',views.home_ti_go,name='home_ti')
]

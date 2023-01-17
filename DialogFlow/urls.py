
from django.contrib import admin
from django.urls import path,include
from chatapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.ChatAppView)
]

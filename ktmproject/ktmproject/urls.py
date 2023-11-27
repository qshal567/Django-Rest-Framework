
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentinfo/', views.student_data),
    path('studentinfo/', views.student_list),
]

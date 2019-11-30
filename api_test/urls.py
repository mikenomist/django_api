from django.urls import path
from api_test import views

app_name = 'api_test'

urlpatterns = [
    # 一覧
#    path('', views.main_view, name='main'),
    path('', views.init_request, name='main'),
    path('api/count/', views.api_count_request, name='api'),
]

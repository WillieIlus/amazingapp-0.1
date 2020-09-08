from django.urls import path

from .views import BlogDetail, BlogList

app_name = 'Blog'

urlpatterns = [
    path('<pk>/', BlogDetail.as_view(), name='detail'),
    path('', BlogList.as_view(), name='list'),
]

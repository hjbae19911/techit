from django.urls import path

from articleapp.views import TempView, ArticleCreateView, ArticleDetailView

app_name = 'articleapp'

urlpatterns = [

    path('temp/', TempView.as_view(), name='temp'),

    path('create/', ArticleCreateView.as_view(), name='create'),
    path('detail/', ArticleDetailView.as_view(), name='detail'),

]
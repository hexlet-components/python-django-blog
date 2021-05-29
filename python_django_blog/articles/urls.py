from django.urls import path
from python_django_blog.articles import views

app_name = 'articles'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.ArticleCreate.as_view(), name='create'),
    path('<int:pk>/delete/', views.ArticleDelete.as_view(), name='delete'),
    path('<int:pk>/update/', views.ArticleUpdate.as_view(), name='update'),
    path('<int:pk>/', views.ArticleDetail.as_view(), name='detail'),
]

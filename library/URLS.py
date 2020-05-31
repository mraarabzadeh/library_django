from django.contrib import admin
from django.urls import path, include

from library import views

urlpatterns = [
    path('signup/', views.SignUp, name='signup'),
    path('Signup/', views.SignUpClass.as_view(), name='Signup'),
    path('addbook/', views.AddBook, name='addbook'),
    path('', views.HomePage, name='base'),
    path('searchbook/', views.SearchBook, name='searchbook'),
    # path('showbookresult/', views.ShowBookResult, name='showbookresult'),

]

from django.contrib import admin
from . import views
from django.urls import path,include


urlpatterns= [
    path('',views.DiaryList.as_view()),
    path('<int:pk>/',views.DiaryDetail.as_view()),
    path('update_diary/<int:pk>',views.DiaryUpdate.as_view()),
    path('create_diary/',views.DiaryCreate.as_view()),
    path('category/<str:slug>/',views.categories),
    path('<int:pk>/add_comment/',views.comment_upload),
]


from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_pk>/details', views.details, name='details'),
    path('<int:question_pk>/results', views.results, name='results'),
    path('<int:question_pk>/votes', views.votes, name='votes'),
]

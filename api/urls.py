from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('portfolio/', views.PortfolioList.as_view()),
    path('our-team/', views.TeamList.as_view()),
    path('message-create/', views.message_create),
    path('vacancy-list/', views.VacancyList.as_view()),
    path('vacancy-detail/<int:pk>/', views.VacancyDetail.as_view()),
    path('resume-create/', views.vacancy_resume),
]

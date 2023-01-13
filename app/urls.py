from django.urls import re_path
import views

urlpatterns = [
    re_path('^$', views.home, name='home'),
    re_path('demand/', views.demand, nome='demand'),
    re_path('geo/', views.geo, name='geo'),
    re_path('skills/', views.skills, name='skills'),
    re_path('latest_vacancies/', views.vacancies, name='latest_vacancies')
]

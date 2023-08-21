from django.urls import path
from . import views
urlpatterns = [
    path('', views.index , name='home' ),
    path('request/', views.request ,name='request'),
    path('signup/', views.signup ,name='signup'),
    path('europ/', views.europ , name='europ'),
    path('admine/', views.admine ,name='admine'),
    path('logout/', views.logoutUser ,name='logout'),
    path('dashboard/', views.dashboard ,name='dashboard'),
    path('News/', views.News ,name='News'),
    path('carte/', views.create_carte ,name='carte'),
    path('tube/', views.tube,name='tube'),


]

from django.urls import path
from . import views
urlpatterns = [
    path('', views.index , name='home' ),
    path('request/', views.request ,name='request'),
    path('signup/', views.signup ,name='signup'),
    path('europ/', views.europ , name='europ'),
    path('liste/', views.liste ,name='liste'),
    path('orders/', views.orders ,name='orders'),
    path('order_europe/', views.order_europe ,name='order_europe'),
    path('admine/', views.admine ,name='admine'),
    path('registre/', views.registrePage ,name='registrePage'),
    path('logout/', views.logoutUser ,name='logout'),
    path('dashboard/', views.dashboard ,name='dashboard'),
    path('news/', views.news ,name='news'),


]

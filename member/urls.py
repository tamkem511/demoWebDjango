from django.urls import path
from . import views
app_name = "member"
urlpatterns = [
    path('register/',views.addUser.as_view(),name = "user"),
    path('login/',views.loginUser.as_view(),name = "login"),
    path('logout/',views.logOut,name = 'logout'),
    path('homePage/',views.homePage.as_view(),name = 'homePage')
]
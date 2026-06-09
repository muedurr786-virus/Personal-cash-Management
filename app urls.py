from django.urls import path
from .views import *

urlpatterns = [
    path("register/", registerPage, name="registerPage"),
    path("", loginPage, name="loginPage"),
    path("logout/", logoutPage, name="logoutPage"),
    path("dashboardpage/", dashboardpage, name="dashboardpage"),
    path("profile/", profilePage, name="profilePage"),
    path("add-cash/", addCashPage, name="addCashPage"),
    path("expend-cash/", expendCashPage, name="expendCashPage"),
]


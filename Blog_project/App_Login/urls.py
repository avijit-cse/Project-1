from django.urls import path
from App_Login import views


urlpatterns = [
    path('',views.sing_up,name="sing_up"),
    path('singin/',views.log_in,name="login"),
    path('logout/',views.logout_page,name="logout"),
    path('profile/',views.profile_view,name="profile"),
    path('change/',views.user_change,name="change"),
    path('password/',views.password_change,name="password"),
    path('addpic/',views.add_pro_pic,name="addpic"),
    path('changepic/',views.change_pro_pic,name="changepic"),
]




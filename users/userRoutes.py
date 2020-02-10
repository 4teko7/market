from django.conf.urls import url
from django.contrib import admin
from users.userViews import *
app_name = "userroutes"
urlpatterns = [
    url("about/(?P<id>\d+)/",about,name = "about"),
    url("register/",registerUser,name = "registerUser"),
    url("login/",loginUser,name = "loginUser"),
    url("logout/",logoutUser,name = "logoutUser"),
    url("editprofile/",editProfile,name = "editprofile"),
    url("saveprofile/",saveProfile,name = "saveprofile"),
    url("changepassword/",changePassword,name = "changepassword"),
    url("changeusername/",changeUsername,name = "changeusername"),
    url("profile/(?P<id>\d+)/",profile,name = "profile"),
    url("addprofileimage/",addProfileImage,name = "addprofileimage"),
    url("buyproduct/(?P<id>\d+)/",buyProduct,name = "buyproduct"),
    url("orderreceived/(?P<id>\d+)/",orderReceived,name = "orderreceived"),
    url("preparing/(?P<id>\d+)/",preparing,name = "preparing"),
    url("shipped/(?P<id>\d+)/",shipped,name = "shipped"),
    url("delivered/(?P<id>\d+)/",delivered,name = "delivered"),
    url("completed/(?P<id>\d+)/",completed,name = "completed"),
]
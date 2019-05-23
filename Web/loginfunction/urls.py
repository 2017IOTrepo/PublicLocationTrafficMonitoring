from django.conf.urls import url
from loginfunction.views import LoginForm,register,userlogin,clean,part_flush
# from loginfunction.views import login
urlpatterns = [
    url(r'^$',userlogin,name="login"),
    url(r'^register/$',register,name="register"),
    url(r'^clean/$',clean,name="clean"),
]
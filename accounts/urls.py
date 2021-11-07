from django.urls import path
from .views import Reistration,LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', Reistration.as_view(), name="registration"),
]


"""
http://127.0.0.1:8000/accounts/login/
http://127.0.0.1:8000/accounts/registration/

"""


from django.contrib import admin
from django.urls import path, include
from shorturl.views import Redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("shorturl.urls")),
    path('accounts/', include("accounts.urls")),
    path("<str:shortUrl>/", Redirect.as_view(), name="Redirect"),

]
